from scrapy import Item, Field
class AdvancedSearchParam(Item):

    #搜索关键词
    keyword = Field()

    #搜索的标签
    type = Field()
    sub = Field()

    #总的时间跨度
    year_start = Field()
    year_end = Field()
    month_start = Field()
    day_start = Field()
    month_end = Field()
    day_end = Field()

    #每次搜索的时间步长
    day_step = Field()

    #每个时间步长爬取的页数
    page_start = Field()
    page_end = Field()
