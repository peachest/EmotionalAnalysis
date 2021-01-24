# -*- coding: utf-8 -*-
# https://blog.csdn.net/weixin_43873702/article/details/111473656?utm_medium=distribute.pc_relevant.none-task-blog-OPENSEARCH-8.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-OPENSEARCH-8.control
import random
import re
import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from AdvancedSearchParam import AdvancedSearchParam
from AdvancedURLParser import AdvancedURLParser
from dataCleaner import dataCleaner
from weiboDataExporter import csvExporter


class seleniumCrawler:
    """
    """

    def __init__(self, exportPath, enable_picture_and_css_load=True):
        print("正在初始化爬虫。。。")
        # 设置导出
        self.exportPath = exportPath
        self.exporter = csvExporter(self.exportPath)
        print("导出数据到路径: " + self.exportPath)

        # 设置是否允许加载图片
        option = webdriver.ChromeOptions()
        if enable_picture_and_css_load:
            option.add_experimental_option('excludeSwitches', ['enable-automation'])
            print("允许 加载图片和CSS")
        else:
            # 禁止图片和css加载
            prefs = {"profile.managed_default_content_settings.images": 2}
            option.add_experimental_option("prefs", prefs)
            print("不允许 加载图片和CSS")
        self.browser = webdriver.Chrome(options=option)

        # 最大化窗口
        self.browser.maximize_window()
        # 设置等待网页与元素加载的时间，如果一直加载不出就等10秒，加载好了就立刻结束等待
        # 防止元素还没加载出来就开始爬。
        self.browser.implicitly_wait(5)
        print("初始化完成")

    def login(self, username, password):
        '''
        进行登录
        '''
        print("开始登陆")
        # 进入微博首页进行登录
        self.browser.get(
            "https://s.weibo.com")  # self.wb.get("https://s.weibo.com/weibo/%25E8%2582%25BA%25E7%2582%258E?topnav=1&wvr=6&b=1")

        # 点击登录、输入账号密码、点击确认登录
        self.browser.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[3]/div[2]/ul/li[3]/a').click()
        self.browser.find_element_by_xpath('//div[@class="item username input_wrap"]/input').send_keys(username)
        self.browser.find_element_by_xpath('//div[@class="item password input_wrap"]/input').send_keys(password)
        self.browser.find_element_by_xpath('//div[@class="item_btn"]/a').click()  # 手机应用扫一扫登录

        # 从上一个click开始等待10sec，进行扫一扫操作，避免出现未完成登录就跳转下一个页面使得登录失败
        time.sleep(15)
        print("登陆完成")

    def turnToPage(self, url):
        print('页面跳转中...')
        self.browser.get(url)
        print('页面跳转完成')

    def lowb_search(self):
        pass

    def AdvancedSearch(self, param):
        print("开始进行高级搜索")

        # 类型判断
        if (not isinstance(param, AdvancedSearchParam)):
            print("param in method AdvancedSearch must be instance of \'dict\'")
            print("please retry")
            return

        urlParser = AdvancedURLParser(param)
        url = urlParser.getFirstURL()
        self.urlCount = 1
        while (True):
            if (url == None):  # 退出条件
                break

            # 准备爬取
            self.browser.get(url)
            print("正在爬取第 " + str(self.urlCount) + " 个页面...")

            # 错误检测
            errorCount = 0
            try:
                errorTxt = ""
                merror = self.browser.find_element_by_xpath('//div[@class="card card-no-result s-pt20b40"]/p')
                errorTxt = merror.text
                # print(errorTxt)
                if (errorTxt[0] == '抱' and errorTxt[1] == '歉'):
                    errorCount += 1
                if (errorCount > 4):
                    break;
                continue
            except:
                pass

            # 爬取当前页的数据，并导出
            pageData = self.crawlCurrentIndexPage()
            print(pageData[0])
            print(pageData[1])
            print(pageData[2])
            print(pageData[3])
            print(pageData[4])
            print(pageData[5])
            self.exporter.export(pageData[0],
                                 pageData[1],
                                 pageData[2],
                                 pageData[3],
                                 pageData[4],
                                 pageData[5])

            # 准备下一个循环
            time.sleep(random.random() * 1.2)
            url = urlParser.getNextURL()
            print(url)
            self.urlCount += 1
            pass

    def crawlCurrentIndexPage(self):
        '''
        用新标签页打开当前页每个微博的评论区，在该标签页中爬取所需信息
        '''

        blogTexts = []
        blogTimes = []
        blogForwardNums = []
        blogCommentNums = []
        blogLikeNums = []
        blogCommentss = []

        indexPageHandle = self.browser.current_window_handle
        for i in range(1, 30):
            xpath = '//*[@id="pl_feedlist_index"]/div[2]/div[' + str(i) + ']'
            try:
                # 打开新标签页
                element = spider.browser.find_element_by_xpath(xpath + '/div/div[2]/ul/li[3]/a')
                element.click()  # 模拟鼠标点击“评论”

                try:
                    element = spider.browser.find_element_by_xpath(xpath + '/div/div[3]/div/div[3]/a')
                    actions = ActionChains(self.browser)
                    actions.key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()  # 模拟鼠标点击“后面还有*条评论，点击查看”
                    print("成功打开标签页")
                except  selenium.common.exceptions.NoSuchElementException:
                    continue

                # 爬取当前标签页
                self.browser.switch_to.window(self.browser.window_handles[-1])
                time.sleep(2)
                blogText, blogTime, forwardNum, commentNum, likeNum, comments = self.crawlCurrentBlogPage()
                if(blogText != None and                    blogTimes != None and                    blogForwardNums != None and
                    blogCommentNums != None and                    blogLikeNums != None and                    blogCommentss != None):
                    print("正在记录信息")
                    blogTexts.append(blogText)
                    blogTimes.append(blogTime)
                    blogForwardNums.append(forwardNum)
                    blogCommentNums.append(commentNum)
                    blogLikeNums.append(likeNum)
                    blogCommentss.append(comments)
                # 返回索引页
                time.sleep(1)
                print("返回索引页")
                self.browser.close()
                self.browser.switch_to.window(indexPageHandle)
            except selenium.common.exceptions.NoSuchElementException:
                print('已经点开所有的评论')
                break
        return blogTexts, blogTimes, blogForwardNums, blogCommentNums, blogLikeNums, blogCommentss

    def crawlCurrentBlogPage(self):
        print("正在爬取当前页")
        text = None
        time = None
        forwardNum = None
        commentNum = None
        likeNum = None
        comments = []

        flag = False
        try:
            # text = self.browser.find_element_by_xpath(
            #     '//*[@id="Pl_Official_WeiboDetail__58"]/div/div/div/div[1]/div[4]/div[4]').text
            text = self.browser.find_element_by_xpath(
                '//*[contains(@id, "Pl_Official_WeiboDetail")]'
                '/div[@node-type="feed_list"]/div[@node-type="feedconfig"]/div[@action-type="feed_list_item"]'
                '/div[@node-type="feed_content"]/div[@class="WB_detail"]/div[@node-type="feed_list_content"]').text
            text = self.cleanBlogText(text)
            flag = True
            #print("查找text成功")
        except selenium.common.exceptions.NoSuchElementException:
            print('第一次尝试查找text失败')

        if (flag == False):
            return None, None, None, None, None, None
        try:
            time = self.browser.find_element_by_xpath(
                '//*[contains(@id, "Pl_Official_WeiboDetail")]'
                '/div[@node-type="feed_list"]/div[@node-type="feedconfig"]/div[@action-type="feed_list_item"]'
                '/div[@node-type="feed_content"]/div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a'
            ).get_attribute('title')
            #print('尝试查找' + 'time' + '成功')
            forwardNum = self.browser.find_element_by_xpath(
                '//*[contains(@id, "Pl_Official_WeiboDetail")]'
                '/div[@node-type="feed_list"]/div[@node-type="feedconfig"]/div[@action-type="feed_list_item"]'
                '/div[@class="WB_feed_handle"]/div[@class="WB_handle"]/ul/li[2]/a/span/span/span/em[2]'
            ).text
            #print('尝试查找' + 'forwardNum' + '成功')
            commentNum = self.browser.find_element_by_xpath(
                '//*[contains(@id, "Pl_Official_WeiboDetail")]'
                '/div[@node-type="feed_list"]/div[@node-type="feedconfig"]/div[@action-type="feed_list_item"]'
                '/div[@class="WB_feed_handle"]/div[@class="WB_handle"]/ul/li[3]/a/span/span/span/em[2]'
            ).text
            #print('尝试查找' + 'commentNum' + '成功')
            likeNum = self.browser.find_element_by_xpath(
                '//*[contains(@id, "Pl_Official_WeiboDetail")]'
                '/div[@node-type="feed_list"]/div[@node-type="feedconfig"]/div[@action-type="feed_list_item"]'
                '/div[@class="WB_feed_handle"]/div[@class="WB_handle"]/ul/li[4]/a/span/span/span/em[2]'
            ).text
            #print('尝试查找' + 'likeNum' + '成功')
            print('爬取微博信息成功')
        except:
            return None, None, None, None, None, None

        print('开始爬评论')
        validCommentNum = 0
        allRootCommentElements = self.browser.find_elements_by_xpath('//*[@node-type="root_comment"]')
        #print("尝试寻找所有comment成功")
        for rootCommentElement in allRootCommentElements:
            if (validCommentNum >= 10): break
            commentLikeNum = rootCommentElement.find_element_by_xpath(
                './/*[@node-type="like_status"]/em[2]').text
            if (commentLikeNum == '赞'): commentLikeNum = 0;
            commentText = rootCommentElement.find_element_by_xpath(
                './div[@node-type="replywrap"]/div[@class="WB_text"]').text
            cleanedCommentText = self.cleanCommentText(commentText)
            if (cleanedCommentText == None): continue
            validCommentNum += 1
            #print('爬取到第' + str(validCommentNum) + '个有效评论')
            comment = {'text': cleanedCommentText, 'likeNum': int(commentLikeNum)}
            comments.append(comment)
            pass

        print('当前标签页所有信息爬取成功')
        print('text: ' + text)
        print('time: ' + time)
        print('forwardNum: ' + forwardNum)
        print('commentNum: ' + commentNum)
        print('likeNum: ' + likeNum)
        print('comments: ', end='')
        print(comments)
        return text, time, forwardNum, commentNum, likeNum, comments

    def cleanBlogText(self, str):
        s = re.sub(r'【.*?】|#.*?#|（.*?）', '', str)  # 删除【】，（），##及其中的内容
        s = re.sub(r'([0-9]{1,4}[年月日])|以来|上午|下午|晚上|近期','',s)  # 删除日期
        s = re.sub(r'L.*', '', s)  # 删除微博超链接
        s = re.sub(r'(@.*?\s)', '', s)  # 删除@及其后的内容
        s = dataCleaner.findAllChineseCharacter(s)
        return s

    def cleanCommentText(self, str):
        s = str[str.index('：') + 1:]  # 去掉评论中的用户名与‘：’
        s = dataCleaner.findAllChineseCharacter(s)
        return s

if (__name__ == "__main__"):
    username = "houyx2012@126.com"
    password = "1336jkl;29492"
    exportPath = "weiboData.csv"
    enable_picture_and_css_load = True

    # 设置高级搜索的关键词
    param = AdvancedSearchParam()
    param["keyword"] = "肺炎"

    ##高级搜索中的类型
    # 请将选择一个标签，将冒号后的字符串（包括引号）复制到param中
    # 全部: "typeall=1"
    # 热门: "xsort=hot"
    # 原创: "scope=ori"
    # 关注人: "atten=1"
    # 认证用户: "vip=1"
    # 媒体: "category=4"
    # 观点: "viewpoint=1"
    # #
    param["type"] = "xsort=hot"

    ##高级搜索中的包含
    # 请将选择一个标签，将冒号后的字符串（包括引号）复制到param中
    # 全部: "suball=1"
    # 含图片: "haspic=1"
    # 含视频: "hasvideo=1"
    # 含音乐: "hasmusic=1"
    # 含短链: "haslink=1"
    # #
    param["sub"] = "suball=1"

    # 总的时间跨度
    param["year_start"] = 2020
    param["year_end"] = 2020
    param["month_start"] = 1
    param["day_start"] = 1
    param["month_end"] = 6
    param["day_end"] = 31

    # 每次搜索的时间步长
    param["day_step"] = 1

    # 每个时间步长爬取的页数
    param["page_start"] = 1
    param["page_end"] = 1

    spider = seleniumCrawler(exportPath, enable_picture_and_css_load)
    spider.login(username, password)
    spider.AdvancedSearch(param)
