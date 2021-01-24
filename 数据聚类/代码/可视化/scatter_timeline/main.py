# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

from plotter import *

coordinate_data = []
for time in range(1, 4):
    sector = []
    for category in range(1, 4):
        file = open("time0{}_coordinate_category_0{}.txt".format(time, category), 'r')
        category_data = []
        for line in file.readlines():
            victor = []
            if len(line) == 0:
                continue
            if line == '\n':
                continue
            line_data = line.split()
            for item in line_data:
                if len(item) == 0:
                    continue
                victor.append(float(item))
            category_data.append(victor)

        sector.append(category_data)
    coordinate_data.append(sector)

plot(coordinate_data)

