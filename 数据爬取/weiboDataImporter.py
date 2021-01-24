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
    reader = weiboDataImporter("weiboData.csv")
    blogs = reader.importData()


