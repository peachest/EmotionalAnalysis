<center><h1>EmotionalAnalysis</h1></center>

[TOC]

## Description

​	Project of Data Science. Take weibo as an example to analyse public emotional orientation.

​	This project has been splited into three parts, and each part is complete by one person. All the programs and middle results have been stored as csv or txt file in the folders. Each part has its own   readme file which describes the program clearly.

​	The report of this project is written by typora and export as html file. The visualization in the report is rendered as html file too and stored in the '\.assets' folder,  so don't change the report folder at any time otherwise the report can't show correctly. 

## Basic idea

​	This experiment takes "pneumonia" as the keyword and crawls the text of weibo search website as the original data. 

​	The initial processing of the data crawled down includes deleting the title, time, quoted tag and hyperlink in the text of weibo, and deleting all the non-Chinese-characters in the text of weibo and its comments. The initially processed data is divided into four  portions according to the release time.

​	 For each time period, on the one hand, the stuttering segmentation is used to get the word segmentation set, and the TF-IDF method is used to calculate the weight of the word segmentation set through which the top 50 words with the largest weight are extracted as the feature words of all the texts in the time period; on the other hand, based on the emotional words The emotional intensity of the feature words is calculated by the pre-defined formula of emotional words dictionary and  emotional value, and then the Emotional Value of the text and the Intensity of Sentiment Orientation of the text are calculated.

​	Combined with the Intensity of Sentiment Orientation, the weight of feature words in each text is calculated, and the emotional feature vector of each text is constructed to form the emotional feature matrix. 

​	Finally, K-means clustering algorithm is used to cluster the data. PCA is used to reduce the dimension of clustering results and then visualize them.