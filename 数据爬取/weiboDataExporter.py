import csv
class csvExporter:

    #初始化，设置字段名，并且在文件第一行写入字段
    def __init__(self, filePath):
        self.filePath = filePath
        self.fieldNames = ['blogText',
                           'blogTime',
                           'blogForwardNum',
                           'blogCommentNum',
                           'blogLikeNum',
                           ]
        for i in range(1, 11):
            self.fieldNames.append('comment_' + str(i) + '_text')
            self.fieldNames.append('comment_' + str(i) + '_likeNum')
        with open(self.filePath, 'w', newline='',  encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldNames)
            writer.writeheader()


    def export(self, blogTexts, blogTimes,
                       blogForwardNums, blogCommentNums, blogLikeNums,
                       blogCommentss):
        print('正在导出数据')
        with open(self.filePath, 'a', newline='',  encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldNames)
            for text, time, forwardNum, commentNum, likeNum, blogComments in zip(blogTexts, blogTimes, blogForwardNums, blogCommentNums, blogLikeNums, blogCommentss):
                row = {}
                row['blogText'] = text
                row['blogTime'] = time
                row['blogForwardNum'] = forwardNum
                row['blogCommentNum'] = commentNum
                row['blogLikeNum'] = likeNum
                for i, comment in enumerate(blogComments):
                    row['comment_' + str(i+1) + '_text'] = comment['text']
                    row['comment_' + str(i+1) + '_likeNum'] = comment['likeNum']
                writer.writerow(row)
            print('导出数据完成')
    def dataPrepare(self):
        text = ['a', 'b', 'c']
        time = [1, 2, 3]
        forwadNum = [1, 2, 3]
        commentNum = [1, 2, 3]
        likeNum = [1, 2, 3]
        comments = [[{'text': 'a', 'likeNum': 1},
                     {'text': 'b', 'likeNum': 2},
                     {'text': 'c', 'likeNum': 3}, ],

                    [{'text': 'a', 'likeNum': 1},
                     {'text': 'b', 'likeNum': 2},
                     {'text': 'c', 'likeNum': 3}, ],

                    [{'text': 'a', 'likeNum': 1}, ]
                    ]
        return text, time, forwadNum, commentNum, likeNum, comments
if(__name__ == "__main__"):
    e = csvExporter("testcsvExporter.csv")
    data = e.dataPrepare()
    e.export(data[0],
             data[1],
             data[2],
             data[3],
             data[4],
             data[5],)