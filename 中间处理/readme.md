<center><h1>中间数据处理</h1>
</center>

[TOC]

## 项目的类

```python
#weiboDataImporter.py
class weiboDataImporter():
    def __init__(self, path)
    def importData(self)
```

```python
#weiboBlog.py
class weiboBlog:
    #重载
    def __init__(self, row):
    def __str__(self):
        
    #各种getter
    def get_blogText(self)
    def get_blogTime(self)
    def get_blogForwardNum(self)
    def get_blogCommentNum(self
    def get_blogLikeNum(self)
    def get_comments(self)
    def get_comment_indexOf(self, index)

	#根据文本数据计算文本热度，赋予文本一个二次加权的权重
	def quadratic_weighted_value(self, blogForwardNum, blogCommentNum, blogLikeNum)
```

```python
#数据处理与计算.py

#调用jieba库的cut方法
def cutByJieba(file, target)

#调用jieba库的analyse.extract_tags方法进行TF-IDF提取特征词
def findTheKeyword(file_path, target_path, num, isWithWeight)

#累加文本中的特征词的情感强度，计算出每个文本的情感值
def culEmotionalValue(file_path, target_path)

#根据每个文本的权重进行二次加权
def reCluEmotionalValue(first_value_path, weight_value_path, target_path)

#进行中间结果的输出
def filterTextAndLine(file_path, target_path)

#对所有文本的情感值计算其文本的情感倾向强度
def cluISO(file_path, target_path)

#进行中间结果输出
def combineCommentAndISOToCSV(comment_path, ISO_path, csv_path)

#计算每个文本的情感特征向量，对每个文本进行ont-hot编码
def cluVector(comment_and_ISO_path, frequency_and_TFIDF_path, target_path)

#输出中间结果
def takeCommentAndVector(comment_ISO_path, vector_path, target_path)
```

## 程序入口

```python
#数据处理与计算.py
#main 函数
if (__name__ == '__main__')
```

## 数据流

 	1. 利用weiboDataImporter读取爬取的数据，将每条微博及其下评论创建为一个weiboBlog对象，将所有weiboBlog按照发布时间分成四个时间段的类别，对每个时间段的数据进行下列处理
 	2. 对所有文本，结合停用词词典，进行结巴分词
 	3. 利用TF-IDF寻找tf-idf值最大的前50个特征词
 	4. 用情感词词典对每个文本中的特征词进行碰撞，若碰撞成功，根据特征词前的程度副词以及否定词计算特征词的情感值，累计该文本所有特征情感词的情感值作为该文本的情感词
 	5. 计算每个文本的情感倾向强度
 	6. 构建每个文本的情感特征向量，形成超高维的情感特征矩阵

