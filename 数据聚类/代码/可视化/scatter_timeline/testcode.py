# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

from pyecharts.charts import Scatter3D, Timeline
import pyecharts.options as opts

data1 = [
    [1, 3, 5],
    [2, 4, 6],
    [0, 1, 2]
]

data2 = [
    [2, 3, 4],
    [3, 3, 5],
    [3, 4, 6]
]

timeline = Timeline()

file = open("time01_coordinate_category_01.txt", 'r')
data4 = []
for line in file.readlines():
    if len(line) == 0:
        continue
    if line == '\n':
        continue
    victor = []
    for item in line.split():
        victor.append(float(item))
    data4.append(victor)

scatter1 = (
    Scatter3D(init_opts=opts.InitOpts(width="1440px", height="720px"))
    .add(
        series_name="模拟点位",
        data=data1,
        xaxis3d_opts=opts.Axis3DOpts(
            name="x_axis",
            type_="value"
        ),
        yaxis3d_opts=opts.Axis3DOpts(
            name="y_axis",
            type_="value"
        ),
        zaxis3d_opts=opts.Axis3DOpts(
            name="z_axis",
            type_="value"
        ),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
    )
    # .add(series_name="模拟点位2",
    #     data=data2,
    #     xaxis3d_opts=opts.Axis3DOpts(
    #         name="x_axis",
    #         type_="value"
    #     ),
    #     yaxis3d_opts=opts.Axis3DOpts(
    #         name="y_axis",
    #         type_="value"
    #     ),
    #     zaxis3d_opts=opts.Axis3DOpts(
    #         name="z_axis",
    #         type_="value"
    #     ),
    #     grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100))
    .set_global_opts(title_opts=opts.TitleOpts(title="示例散点图"))
)
timeline.add(scatter1, "time01")

scatter2 = (
    Scatter3D(init_opts=opts.InitOpts(width="1440px", height="720px"))
    .add(
        series_name="模拟点位",
        data=data2,
        xaxis3d_opts=opts.Axis3DOpts(
            name="x_axis",
            type_="value"
        ),
        yaxis3d_opts=opts.Axis3DOpts(
            name="y_axis",
            type_="value"
        ),
        zaxis3d_opts=opts.Axis3DOpts(
            name="z_axis",
            type_="value"
        ),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="示例散点图"))
)
timeline.add(scatter2, "time02")

timeline.render("test.html")

# scatter.render("test.html")