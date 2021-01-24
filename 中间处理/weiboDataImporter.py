import csv
from weiboBlog import weiboBlog
class weiboDataImporter():

    def __init__(self, path):
        self.filePath = path
        pass

    def importData(self):
        blogs = []
        with open(self.filePath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                blog = weiboBlog(row)
                print(blog)
                blogs.append(blog)

        pass
    pass
if (__name__ == "__main__"):
    for i in range(1,5): #清空原有数据

        file=open("时期"+str(i)+".txt", "w")
        file.close()
        file=open("权值"+str(i)+".txt", "w")
        file.close()

    reader = weiboDataImporter("weiboData.csv")
    blogs = reader.importData()













