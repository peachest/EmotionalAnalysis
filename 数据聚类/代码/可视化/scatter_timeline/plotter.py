# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

from pyecharts.charts import Scatter3D, Page
import pyecharts.options as opts
import scatter_of_time_4
import three_means_scatter_of_time_04

def plot(data_in_4_sector):
    # timeline = Timeline()
    name_list = ["1月1日至1月20日", "1月21日至2月23日", "2月24日至3月31日", "4月1日至6月30日"]
    page = Page(layout=Page.SimplePageLayout)
    count = 0
    for sector in range(3):
        scatter3d = (
            Scatter3D(init_opts= opts.InitOpts(width="900px", height="600px"))
            .add(
                series_name="category_01",
                data=data_in_4_sector[sector][0],
                grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
            )
            .add(
                series_name="category_02",
                data=data_in_4_sector[sector][1],
                grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
            )
            .add(
                series_name="category_03",
                data=data_in_4_sector[sector][2],
                grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="经过PCA降维后的三维数据分布图", subtitle=name_list[count], pos_bottom=20))
        )
        page.add(scatter3d)
        count += 1

    page.add(scatter_of_time_4.get_scatter())
    page.add(three_means_scatter_of_time_04.get_scatter())
    page.render("page_layout.html")