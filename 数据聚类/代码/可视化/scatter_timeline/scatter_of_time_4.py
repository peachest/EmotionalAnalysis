# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/24
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8
from pyecharts.charts import Scatter3D
from pyecharts import options as opts

def get_scatter():
    time_data = []
    for category in range(1, 5):
        file = open("time04_coordinate_category_0{}.txt".format(category), 'r')
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
        time_data.append(category_data)

    scatter3d = (
        Scatter3D(init_opts=opts.InitOpts(width="900px", height="600px"))
        .add(
            series_name="category_01",
            data=time_data[0],
            grid3d_opts=opts.Grid3DOpts(width=100, depth=100, height=100)
        )
        .add(
            series_name="category_02",
            data=time_data[1],
            grid3d_opts=opts.Grid3DOpts(width=100, depth=100, height=100)
        )
        .add(
            series_name="category_03",
            data=time_data[2],
            grid3d_opts=opts.Grid3DOpts(width=100, depth=100, height=100)
        )
        .add(
            series_name="category_04",
            data=time_data[3],
            grid3d_opts=opts.Grid3DOpts(width=100, depth=100, height=100)
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="经过PCA降维后的三维数据分布图", subtitle="4月1日至6月30日", pos_bottom=20))
    )

    return scatter3d