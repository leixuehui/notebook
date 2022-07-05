Image Knowledge
===========================

[![Join the chat at https://gitter.im/guodongxiaren/README](https://badges.gitter.im/guodongxiaren/README.svg)](https://gitter.im/guodongxiaren/README?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


****
	

****
## 目录
* [图像常用知识](#图像常用知识)
* [高通pipline](#高通pipline)
* [MTKpipline](#MTKpipline)

____



图像常用知识 
------
## 图像熵（一维熵）  
  图像熵是一种特征的统计形式，它反映了图像中平均信息量的多少。图像的一维熵表示图像中灰度分布的聚集特征所包含的信息量，令Pi表示图像中灰度值i的结果所占的比例：
    ./CodeCogsEqn.svg

高通pipline
--------







MTKpipline
------











### 普通文本
这是一段普通的文本
### 单行文本
    Hello,大家好，
在一行开头加入1个Tab或者4个空格。
### 文本块
#### 语法1
在连续几行的文本开头加入1个Tab或者4个空格。

    欢迎到访
    很高兴见到您
    祝您，早上好，中午好，下午好，晚安

#### 语法2
使用一对各三个的反引号：
```
欢迎到访
我是C++码农

```

#### 换行
直接回车不能换行，  
可以在上一行文本后面补两个空格，  
这样下一行的文本就换行了。

或者就是在两行文本直接加一个空行。

也能实现换行效果，不过这个行间距有点大。




图片
------
基本格式：
```
![alt](URL title)
```
alt和title即对应HTML中的alt和title属性（都可省略）：
- alt表示图片显示失败时的替换文本
- title表示鼠标悬停在图片时的显示文本（注意这里要加引号）

URL即图片的url地址，如果引用本仓库中的图片，直接使用**相对路径**就可了，如果引用其他github仓库中的图片要注意格式，即：`仓库地址/raw/分支名/图片路径`，如：
```
https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif
```

链接
------
### 链接外部URL

|#|语法|效果|
|---|----|-----|
|1|`[我的博客](http://blog.csdn.net/guodongxiaren "悬停显示")`|[我的博客](http://blog.csdn.net/guodongxiaren "悬停显示")|
|2|`[我的知乎][zhihu] `|[我的知乎][zhihu] |

语法2由两部分组成：
- 第一部分使用两个中括号，[ ]里的标识符（本例中zhihu），可以是数字，字母等的组合，标识符上下对应就行了（**姑且称之为URL标识符**）
- 第二部分标记实际URL。


### 链接本仓库里的URL

|语法|效果|
|----|-----|
|`[我的简介](/example/profile.md)`|[我的简介](/example/profile.md)|
|`[example](./example)`|[example](./example)|

### 图片链接
给图片加链接的本质是混合图片显示语法和普通的链接语法。普通的链接中[ ]内部是链接要显示的文本，而图片链接[ ]里面则是要显示的图片。  
直接混合两种语法当然可以，但是十分啰嗦，为此我们可以使用URL标识符的形式。



## 块引用

### 常用于引用文本
#### 文本摘自《深入理解计算机系统》P27
　令人吃惊的是，在哪种字节顺序是合适的这个问题上，人们表现得非常情绪化。实际上术语“little endian”（小端）和“big endian”（大端）出自Jonathan Swift的《格利佛游记》一书，其中交战的两个派别无法就应该从哪一端打开一个半熟的鸡蛋达成一致。因此，争论沦为关于社会政治的争论。只要选择了一种规则并且始终如一的坚持，其实对于哪种字节排序的选择都是任意的。
> **“端”（endian）的起源**  
以下是Jonathan Swift在1726年关于大小端之争历史的描述：  
“……下面我要告诉你的是，Lilliput和Blefuscu这两大强国在过去36个月里一直在苦战。战争开始是由于以下的原因：我们大家都认为，吃鸡蛋前，原始的方法是打破鸡蛋较大的一端，可是当今的皇帝的祖父小时候吃鸡蛋，一次按古法打鸡蛋时碰巧将一个手指弄破了，因此他的父亲，当时的皇帝，就下了一道敕令，命令全体臣民吃鸡蛋时打破较小的一端，违令者重罚。”


