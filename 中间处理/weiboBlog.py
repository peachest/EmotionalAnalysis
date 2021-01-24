import datetime

class weiboBlog:

    def __init__(self, row):
        self._blogText = row['blogText']
        self._blogTime = row['blogTime']
        self._blogForwardNum = row['blogForwardNum']
        self._blogCommentNum = row['blogCommentNum']
        self._blogLikeNum = row['blogLikeNum']
        self._comments = []
        for i in range(1, 11):
            commentData = {}
            commentData["text"] = row['comment_' + str(i) + '_text']
            commentData["likeNum"] = row['comment_' + str(i) + '_likeNum']
            self._comments.append(commentData)

    def __str__(self):
        s = ""
        s += 'blogText: ' + self._blogText
        s += '\nblogTime: ' + self._blogTime
        s += '\nblogForwardNum: ' + self._blogForwardNum
        s += '\nblogCommentNum: ' + self._blogCommentNum
        s += '\nblogLikeNum: ' + self._blogLikeNum
        for i in range(0, 10):
            c = self._comments[i]
            s += '\ncomment_' + str(i + 1) + '_text: ' + c['text'] + '  comment_' + str(i + 1) + '_likeNum: ' + c[
                'likeNum']



        start1="2020-01-01"
        end1="2020-01-21"
        start2=end1
        end2="2020-02-24"
        start3=end2
        end3="2020-04-01"
        start4=end3
        end4="2020-07-01"
        NO=0
        if ((self._blogTime.__ge__(start1)) and (self._blogTime.__lt__(end1)) and (self.get_blogText() != "")):
            NO=1
        elif((self._blogTime.__ge__(start2)) and (self._blogTime.__lt__(end2)) and (self.get_blogText() != "")):
            NO=2
        elif((self._blogTime.__ge__(start3)) and (self._blogTime.__lt__(end3)) and (self.get_blogText() != "")):
            NO=3
        elif((self._blogTime.__ge__(start4)) and (self._blogTime.__lt__(end4)) and (self.get_blogText() != "")):
            NO=4


        if(NO!=0):

            with open("时期"+str(NO)+".txt", "a") as f:
                if (self._blogText != ""):
                    while ('\n' in self._blogText):
                        self._blogText = self._blogText.replace('\n', "")
                    f.write(self._blogText + '\n')
                    for i in self._comments:
                        if (i['text'] != ''):
                            while ('\n' in i['text']):
                                i['text'] = i['text'].replace('\n', "")
                            f.write(i['text'] + '\n')

                    f.write('\n')

            with open("权值"+str(NO)+".txt", "a") as f:
                value = self.quadratic_weighted_value(self._blogForwardNum, self._blogCommentNum, self._blogLikeNum)
                f.write(value + "\n")



        return s


    def get_blogText(self):
        return self._blogText
    def get_blogTime(self):
        return self._blogTime
    def get_blogForwardNum(self):
        return self._blogForwardNum
    def get_blogCommentNum(self):
        return self._blogCommentNum
    def get_blogLikeNum(self):
        return self._blogLikeNum
    def get_comments(self):
        return self._comments
    def get_comment_indexOf(self, index):
        return self._comments[index]

    def quadratic_weighted_value(self,blogForwardNum,blogCommentNum,blogLikeNum):
        if("万" in blogLikeNum) or("万" in blogForwardNum) or("万" in blogCommentNum): #数据过百万会显示成‘100万+’
            return '1.4'
        if("评论" in blogCommentNum) or ("转发" in blogForwardNum) or ("赞" in blogLikeNum): #有部分评论，转发，赞存储了对应的字符串
            return '1'
        sum=int(blogCommentNum)+int(blogForwardNum)+int(blogLikeNum)
        if(sum<3000) and (sum>=0):
            return '1'
        elif (sum>=3000) and(sum<30000):
            return '1.1'
        elif (sum>=30000) and (sum<100000):
            return '1.2'
        elif sum>=100000:
            return '1.3'


