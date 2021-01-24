import csv

# csv文件的路径
filepath = "testCSV.csv"

# 原始数据
times = [1, 2, 3, 4, 5, 6]
texts = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
forwards = [1, 2, 3, 4, 5, 6]

# 用csv.dictWriter写
with open(filepath, 'w', newline='') as csvfile:  # 参数 newline=''不能动，直接用就行
    # 自定义 字段
    fieldNames = ['blogText', 'blogTime', 'blogForwardNum']
    writer = csv.DictWriter(csvfile, fieldnames=fieldNames)

    # 在Excel第一行写入字段名
    writer.writeheader()

    # 写入每一行的数据
    dict = {}
    for text, time, forwardNum in zip(texts, times, forwards):
        dict['blogText'] = text
        dict['blogTime'] = time
        dict['blogForwardNum'] = forwardNum
        writer.writerow(dict)

# 用csv.dictReader读
with open(filepath, 'r', newline='') as csvfile:  # 参数 newline=''不能动，直接用就行
    reader = csv.DictReader(csvfile)
    for row in reader:
        # 每一行是一个 dict 对象 {key：value}
        print(row)
        print(row['blogTime'])
