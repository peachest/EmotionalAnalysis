# !/usr/bin/env python
# Author Everlearner
# Created 2021/1/22
# User Stephen Zhang
# By PyCharm
# File Encoding Utf-8

from pyecharts.charts import WordCloud, Timeline
from pyecharts import options as opts
from pyecharts.globals import SymbolType

def plot_timeline(data_in_times):
    names = ["1月1日至1月20日", "1月21日至2月23日", "2月24日至3月31日", "4月1日至6月30日"]
    timeline = Timeline()
    count = 0
    for words in data_in_times:
        cloud = (
            WordCloud(init_opts=opts.InitOpts(width="2000px", height="1000px"))
            .add("", words, word_size_range=[10, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="各时间段热点情绪词词云"))
        )
        timeline.add(cloud, names[count])
        count += 1

    timeline.render("timeline.html")