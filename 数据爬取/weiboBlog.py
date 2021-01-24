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
        s +=   'blogText: ' + self._blogText
        s += '\nblogTime: ' + self._blogTime
        s += '\nblogForwardNum: ' + self._blogForwardNum
        s += '\nblogCommentNum: ' + self._blogCommentNum
        s += '\nblogLikeNum: ' + self._blogLikeNum
        for i in range(0, 10):
            c = self._comments[i]
            s += '\ncomment_' + str(i+1) + '_text: ' + c['text'] + '  comment_' + str(i+1)+'_likeNum: ' + c['likeNum']
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
