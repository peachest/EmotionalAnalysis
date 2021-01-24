import AdvancedSearchParam
class AdvancedURLParser:
    def __init__(self, param):
        self.param = param
        self.currentY = param["year_start"]
        self.currentM = param["month_start"]
        self.currentD = param["day_start"]
        self.currentP = param["page_start"]
        self.step = param["day_step"]
        self.calendar = {1:31,
                         3:31,
                         4:30,
                         5:31,
                         6:30,
                         7:31,
                         8:31,
                         9:30,
                         10: 31,
                         11: 30,
                         12: 31}
        pass

    def getURL(self, Y, M, D, P):
        return "https://s.weibo.com/weibo?q={keyword}&{type}&{sub}&timescope=custom:{year_start}-{month_start}-{day_start}:{year_end}-{month_end}-{day_end}&Refer=g&page={page}". \
            format(    keyword = self.param["keyword"],
                          type = self.param["type"],
                           sub = self.param["sub"],

                    year_start = Y,
                   month_start = M,
                     day_start = D,

                      year_end = Y,
                     month_end = M,
                       day_end = D,

                          page = P
                   )

    def getFirstURL(self):
        return self.getNextURL()

    def getNextURL(self):
        #判断是否还在时间范围内
        if(self.isReachTheBoundary()):
            return None

        url = self.getURL(self.currentY,
                          self.currentM,
                          self.currentD,
                          self.currentP)

        #更新下一个url要用的参数
        self.currentP += 1
        if(self.currentP > self.param["page_end"]):
            self.currentP = self.param["page_start"]
            self.currentD += self.step

        dayNums = self.getDayNum()
        if(self.currentD > dayNums):
            self.currentD = 1
            self.currentM += 1

        if(self.currentM > 12):
            self.currentM = 1
            self.currentY += 1
        return url

    def getDayNum(self):
        if(self.currentM == 2):#二月份特殊处理
            y = self.currentY
            if(((y % 100 == 0)and(y % 400 == 0)) or (y % 4 == 0)):#判断闰年
                return 29
            else: #不是闰年
                return 28
        else:
            return self.calendar.get(self.currentM)

    def isReachTheBoundary(self):
        return  (self.currentY > self.param["year_end"]) \
            or ((self.currentY == self.param["year_end"]) and (self.currentM > self.param["month_end"]))\
            or ((self.currentY == self.param["year_end"]) and (self.currentM == self.param["month_end"]) and (self.currentD > self.param["day_end"])) \
            or ((self.currentY == self.param["year_end"]) and (self.currentM == self.param["month_end"]) and (\
                    self.currentD == self.param["day_end"]) and (self.currentP > self.param["page_end"]))

    pass
