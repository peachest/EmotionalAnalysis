# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

import numpy as np
from sklearn.decomposition import PCA
from matplotlib import pyplot

def pca(data_set):
    pca = PCA(n_components=3)  # 降到2维
    pca.fit(data_set)  # 训练
    newX = pca.fit_transform(data_set)  # 降维后的数据
    # PCA(copy=True, n_components=2, whiten=False)
    print(pca.explained_variance_ratio_)  # 输出贡献率
    # print(newX)
    # for array in newX:
    #     pyplot.scatter(array[0], array[1], c='r')
    #
    # pyplot.show()

    return newX