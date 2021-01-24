# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

import csv
from kmeans import *
from numpy import *
from pca import *

csv_file = open("combine comment and vector\\comment_vector_4.csv", 'r', newline='') # 聚类数据源的文件名
csv_reader = csv.DictReader(csv_file)

comment_content = []
comment_victor_string = []

for row in csv_reader:
    comment_content.append(row["评论"])
    comment_victor_string.append(row["向量"])

comment_victor = []
for line in comment_victor_string:
    victor = []
    items = line.split()
    for item in items:
        if len(item) == 0:
            continue
        victor.append(float(item))

    if len(victor) == 0:
        continue
    comment_victor.append(victor)

arrays = array(comment_victor)

k = 4 
# 聚类的k值，在对时间段4的数据进行聚类时k值为4，其余时间段为3
centroids, cluster_assignment = kmeans(arrays, k)
print(centroids)

coordinate = pca(arrays)

root_string = "time04_"
assignment_01 = 0
assignment_02 = 0
assignment_03 = 0
assignment_04 = 0

comment_file_01 = open(root_string + 'comment_category_01.txt', 'w')
comment_file_02 = open(root_string + "comment_category_02.txt", 'w')
comment_file_03 = open(root_string + "comment_category_03.txt", 'w')
comment_file_04 = open(root_string + "comment_category_04.txt", 'w')
coordinate_file_01 = open(root_string + "coordinate_category_01.txt", 'w')
coordinate_file_02 = open(root_string + "coordinate_category_02.txt", 'w')
coordinate_file_03 = open(root_string + "coordinate_category_03.txt", 'w')
coordinate_file_04 = open(root_string + "coordinate_category_04.txt", 'w')
for index in range(len(cluster_assignment)):
    group = cluster_assignment[index, 0]
    if group == 0.0:
        assignment_01 += 1
        comment_file_01.write(comment_content[index] + '\n')
        coordinate_file_01.write("{} {} {}\n".format(coordinate[index, 0], coordinate[index, 1], coordinate[index, 2]))
    elif group == 1.0:
        assignment_02 += 1
        comment_file_02.write(comment_content[index] + '\n')
        coordinate_file_02.write("{} {} {}\n".format(coordinate[index, 0], coordinate[index, 1], coordinate[index, 2]))
    elif group == 2.0:
        assignment_03 += 1
        comment_file_03.write(comment_content[index] + '\n')
        coordinate_file_03.write("{} {} {}\n".format(coordinate[index, 0], coordinate[index, 1], coordinate[index, 2]))
    elif group == 3.0:
        assignment_04 += 1
        comment_file_04.write(comment_content[index] + '\n')
        coordinate_file_04.write("{} {} {}\n".format(coordinate[index, 0], coordinate[index, 1], coordinate[index, 2]))
    else:
        print("other group")

print("category01: {}".format(assignment_01))
print("category02: {}".format(assignment_02))
print("category03: {}".format(assignment_03))
print("category04: {}".format(assignment_04))
