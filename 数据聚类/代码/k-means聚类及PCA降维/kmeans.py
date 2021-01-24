# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

from joblib.numpy_pickle_utils import xrange
from numpy import *
import time
import matplotlib.pyplot as plt

# 计算欧式距离
def euclDistance(vector1,vector2):
    return sqrt(sum(pow(vector2-vector1, 2)))  # pow()是自带函数

# 使用随机样例初始化质心
def initCentroids(dataSet,k):
    # k是指用户设定的k个种子点
    # dataSet - 此处为mat对象
    numSamples, dim = dataSet.shape
    # numSample - 行，此处代表数据集数量  dim - 列，此处代表维度，例如只有xy轴的，dim=2
    centroids = zeros((k, dim))  # 产生k行，dim列零矩阵
    for i in range(k):
        index = int(random.uniform(0, numSamples))  # 给出一个服从均匀分布的在0~numSamples之间的整数
        centroids[i, :] = dataSet[index, :]  # 第index行作为种子点（质心）
    return centroids

# k均值聚类
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # frist column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    clusterChanged = True

    ## step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        ## for each sample
        for i in xrange(numSamples):
            minDist = 100000.0  # 最小距离
            minIndex = 0  # 最小距离对应的点群
            ## for each centroid
            ## step2: find the centroid who is closest
            for j in range(k):
                if len(centroids[j]) == 0 or len(dataSet[i]) == 0:
                    continue
                distance = euclDistance(centroids[j, :], dataSet[i, :])  # 计算到数据的欧式距离
                if distance < minDist:  # 如果距离小于当前最小距离
                    minDist = distance  # 则最小距离更新
                    minIndex = j  # 对应的点群也会更新

            ## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:  # 如当前数据不属于该点群
                clusterChanged = True  # 聚类操作需要继续
                clusterAssment[i, :] = minIndex, minDist**2

        ## step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:,0].A == j)[0]]  # 取列
            # nonzeros返回的是矩阵中非零的元素的[行号]和[列号]
            # .A是将mat对象转为array
            # 将所有等于当前点群j的，赋给pointsInCluster，之后计算该点群新的中心
            if len(pointsInCluster) == 0:
                continue
            centroids[j, :] = mean(pointsInCluster, axis=0)  #  最后结果为两列，每一列为对应维的算术平方值

    # print "Congratulations, cluster complete!"
    return centroids, clusterAssment