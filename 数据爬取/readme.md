<center><h1>selenium实现的微博爬虫</h1></center>

[TOC]

## 项目的类

~~~python
'''
爬虫主程序
'''
class seleniumCrawler   
	#初始化爬虫
    def __init__(self, exportPath, enable_picture_and_css_load=True)
    
    #利用账号密码登录
    def login(self, username, password)
    
    #接受url并跳转
    def turnToPage(self, url)
    
    #进行高级搜索    
    def AdvancedSearch(self, param)
    
    #从索引页与博文页进行爬取
    def crawlCurrentIndexPage(self)
    def crawlCurrentBlogPage(self)
        
    #数据清洗
    def cleanBlogText(self, str)
    def cleanCommentText(self, str)     
~~~

~~~python
'''
自定义的微博的数据结构，不过没有被用到
'''
class weiboBlog
~~~

```python
from scrapy import Item, Field
'''
自定义高级搜索的参数结构。
继承scrapy框架中的Item类，方便构建所有参数形式的数据结构，基类是python的字典类。
'''
class AdvancedSearchParam(Item) 
```

~~~python
'''
接受AdvancedSearchParam创建参数，为循环爬取提供url
'''
class AdvancedURLParser:
    def __init__(self, AdvancedSearchParam)
    
    #根据固定格式以及年、月、日、页数构建url
    def getURL(self, Y, M, D, P)
    def getFirstURL(self)
    def getNextURL(self)
    
    #获取每个月的日数
    def getDayNum(self)
    
    #判定是否到达时间边界
    def isReachTheBoundary(self)
~~~

```python
'''
接受数据，导出到指定位置
'''
class weiboDataExporter:
    #初始化，设置字段名，并且在文件第一行写入字段
    def __init__(self, filePath)
    
    #blogCommentss: list，储存了10个评论的数据blogComments
    ##blogComments: dict，储存评论文本及点赞数
    def export(self, blogTexts, blogTimes,
                       blogForwardNums, blogCommentNums, blogLikeNums,
                       blogCommentss)
```

## 程序入口

### 程序入口

```python
#seleniumCrawler.py
	if (__name__ == "__main__"):
```

### 参数设置

#### 爬虫参数

```python
#账号密码
username: str 
password: str

#导出路径
exportPath: str

#浏览器驱动是否加载图片与CSS
enable_picture_and_css_load: boolean = True,
```

#### 搜索参数

```python
    # 设置高级搜索的关键词
    param = AdvancedSearchParam()
    
    #搜索关键词
    param["keyword"]: str = "肺炎",

    ##高级搜索中的类型
    # 全部: "typeall=1"
    # 热门: "xsort=hot"
    # 原创: "scope=ori"
    # 关注人: "atten=1"
    # 认证用户: "vip=1"
    # 媒体: "category=4"
    # 观点: "viewpoint=1"
    # #
    param["type"]: str = "typeall=1",

    ##高级搜索中的包含
    # 全部: "suball=1"
    # 含图片: "haspic=1"
    # 含视频: "hasvideo=1"
    # 含音乐: "hasmusic=1"
    # 含短链: "haslink=1"
    # #
    param["sub"]: str = "suball=1",

    #开始时间点
    param["year_start"]: numeric = 2020,        
    param["month_start"]: numeric = 1,
    param["day_start"]: numeric = 1,
    #结束时间点
    param["year_end"]: numeric = 2020,
    param["month_end"]: numeric = 6,
    param["day_end"]: numeric = 31,

    # 每次搜索的时间步长
    param["day_step"]: numeric = 1,

    # 每个时间步长爬取的页数
    param["page_start"]: numeric = 1,
    param["page_end"]: numeric = 1,
```

## 数据流

1. python程序入口，设定所有参数，selenium打开浏览器
2. 利用账号密码，加上手机app扫一扫登录[微博搜索](https://s.weibo.com)网站
3. 使用设定的高级搜索参数创建AdvancedURLParser对象，并利用该对象获取符合爬取条件的所有索引页的url
4. 每个索引页包含20篇微博，为了同时爬取微博以及属于该微博下的评论，用selenium模拟点击每篇微博的评论打开评论区，通过评论区进入属于每篇微博的单独页面
5. 在该页面爬取所需数据。
6. 将所有数据储存进csv文件。

## 数据储存

​	利用python中的csv库中的DictWriter，将爬取下来的数据存放至csv文件中。爬下来的数据用文本文档或者pycharm打开可以正常阅读，但是用WPS的Excel或者windows office的Excel打开时无法将数据分隔到正确的单元格，因此不推荐直接利用Excel打开阅读爬取的数据。储存爬取数据的文件的第一行是数据字段名字，通过使用DictWriter可以达到在csv文件第一行储存字段的效果，也方便处理数据时读取数据。这些字段是读写爬取下来的数据的接口。

​	本次作业的字段接口从左到右如下，：

```python
#微博博文的接口
'blogText', 
'blogTime', 
'blogForwardNum', 
'blogCommentNum', 
'blogLikeNum',

#该博文下10个评论的接口
'comment_1_text'
'comment_1_likeNum'
'comment_2_text'
'comment_2_likeNum'
'comment_3_text'
'comment_3_likeNum'
'comment_4_text'
'comment_4_likeNum'
'comment_5_text'
'comment_5_likeNum'
'comment_6_text'
'comment_6_likeNum'
'comment_7_text'
'comment_7_likeNum'
'comment_8_text'
'comment_8_likeNum'
'comment_9_text'
'comment_9_likeNum'
'comment_10_text'
'comment_10_likeNum'
```



