import os,sys,math
import numpy as np

raw_format = 3337
width = 4096
height = 3072
pack_mode = 'mipi_10b'  #LSI_12b | mipi_12b
is_16bit_align = 1

path = os.getcwd()
file_list = os.listdir(path)
raw_list = []
for file in file_list:
    if '.raw' in file or '.RAWMIPI10' in file and '_out' not in file:
        raw_list.append(file)

depth = 10
if raw_format>=3337 and raw_format<=3340:
    depth = 10
elif raw_format>=3345 and raw_format<=3348:
    depth = 12
elif raw_format>=3393 and raw_format<=3396:
    depth = 14

scale = 1<<(14-depth)

bayer = raw_format%4
[pos_R,pos_Gr,pos_Gb,pos_B] = [0,1,2,3]
if bayer == 1:      #RGGB
    [pos_R,pos_Gr,pos_Gb,pos_B] = [0,1,2,3]
elif bayer == 2:    #GRBG
    [pos_R,pos_Gr,pos_Gb,pos_B] = [1,0,3,2]
elif bayer == 3:    #GBRG
    [pos_R,pos_Gr,pos_Gb,pos_B] = [2,3,0,1]
elif bayer == 0:    #BGGR
    [pos_R,pos_Gr,pos_Gb,pos_B] = [3,2,1,0]

f_csv = open("_check_ob_qc_mipi_raw_separate.csv","w+")
f_csv.write('filename,R,Gr,Gb,B\n')

def raw_unpack(data,width,height,pack_mode,is_16bit_align):
    res = np.zeros((height, width),dtype=np.uint16)
    if pack_mode == 'unpack':
        pitch = width*2
        datasize = pitch*height
        data = data[0:datasize:1]     # 防止在尾部有冗余像素

        pPack0 = data[:, 0:pitch:2]
        pPack1 = data[:, 1:pitch:2]

        pPack0 = pPack0.astype(np.uint16)
        pPack1 = pPack1.astype(np.uint16)
        pUnpack0 = (pPack1 << 8) | pPack0

        res[:, 0:width:1] = pUnpack0

    elif pack_mode == 'mipi_10b':
        pitch = int(width*5/4)
        pitch = (pitch+15)//16*16 #10bit, 16bits 对齐
        datasize = pitch*height
        data = data[0:datasize:1]     # 防止在尾部有冗余像素
        data = data.reshape(height,pitch)

        pPack0 = data[:, 0:pitch:5]
        pPack1 = data[:, 1:pitch:5]
        pPack2 = data[:, 2:pitch:5]
        pPack3 = data[:, 3:pitch:5]
        pPack4 = data[:, 4:pitch:5]

        pPack0 = pPack0.astype(np.uint16)
        pPack1 = pPack1.astype(np.uint16)
        pPack2 = pPack2.astype(np.uint16)
        pPack3 = pPack3.astype(np.uint16)
        pPack4 = pPack4.astype(np.uint16)

        pUnpack0 = (pPack0 << 2) | ((pPack4 >> 0) & 0x03)
        pUnpack1 = (pPack1 << 2) | ((pPack4 >> 2) & 0x03)
        pUnpack2 = (pPack2 << 2) | ((pPack4 >> 4) & 0x03)
        pUnpack3 = (pPack3 << 2) | ((pPack4 >> 6) & 0x03)

        res[:, 0:width:4] = pUnpack0
        res[:, 1:width:4] = pUnpack1
        res[:, 2:width:4] = pUnpack2
        res[:, 3:width:4] = pUnpack3
        
        return res

for i in range(len(raw_list)):
    # width = int(raw_list[i].split('x')[0].split('_')[-1])
    # height = int(raw_list[i].split('x')[1].split('_')[0])

    print(raw_list[i])
    rawdata = np.fromfile(raw_list[i], dtype=np.uint8)
    rawdata = raw_unpack(rawdata,width,height,pack_mode,is_16bit_align)

    data = {}
    data[0] = rawdata[0:height:2,0:width:2]
    data[1] = rawdata[0:height:2,1:width:2]
    data[2] = rawdata[1:height:2,0:width:2]
    data[3] = rawdata[1:height:2,1:width:2]
    
    area = width*height/4

    avg = {}
    for j in range(4):
        sum = np.sum(data[j], dtype=np.double)
        avg[j] = int(sum*scale/area+0.5)

    line = [raw_list[i],avg[pos_R],avg[pos_Gr],avg[pos_Gb],avg[pos_B],'\n']
    line = ','.join(map(str,line))
    f_csv.write(line)

f_csv.close()