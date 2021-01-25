import jieba.analyse
import jieba
import csv



def findTheKeyword(file_path,target_path,num,isWithWeight):

    with open(file_path, 'rb') as f:
        content_bit = f.read()
    tags = jieba.analyse.extract_tags(content_bit, topK=num, withWeight=isWithWeight)

    with open(target_path, 'w', newline='') as csvfile:  # 参数 newline=''不能动，直接用就行
        # 自定义 字段
        if(isWithWeight):
            name=["高频词", "TF-IDF"]
        else:
            name=["高频词"]

        writer = csv.DictWriter(csvfile, fieldnames=name)

        # 在Excel第一行写入字段名
        writer.writeheader()

        # 写入每一行的数据
        dict = {}
        for i in tags:
            dict["高频词"] = i[0]
            if(isWithWeight):
                dict["TF-IDF"] = str(i[1])

            writer.writerow(dict)


def cutByJieba(file,target):
    stop_word_path = "情感词典\\chineseStopWords.txt"
    with open(file,"r") as f:
        lines=f.readlines()
    with open(stop_word_path, "r") as stop:
        r = stop.read()
    with open(target,"w") as f:
        for line in lines:

            isNull = True

            if(line=='\n'):
                f.write('\n')
                continue

            seg=jieba.cut(line,cut_all=False)
            list_seg=list(seg)


            for s in list_seg:
                if(s=='\n') and (not isNull): #isNull防止某一用户的评论被全部过滤，导致依旧写入换行，破坏原有的“评论-换行-评论”结构
                    f.write(s)
                    continue

                if (s not in r):
                    f.write(s+" ")
                    isNull=False


def culEmotionalValue(file_path,target_path):
    with open("情感词典\\副词2倍.txt","r",encoding='utf-8') as f:
        most =f.read()
    with open("情感词典\\副词1.2倍.txt","r",encoding='utf-8') as f:
        more =f.read()
    with open("情感词典\\副词1.25倍.txt","r",encoding='utf-8') as f:
        very =f.read()
    with open("情感词典\\副词1.5倍.txt","r",encoding='utf-8') as f:
        over =f.read()
    with open("情感词典\\副词0.8倍.txt","r",encoding='utf-8') as f:
        little =f.read()
    with open("情感词典\\副词0.5倍.txt","r",encoding='utf-8') as f:
        insufficiently =f.read()

    with open("情感词典\\正面情绪词.txt","r",encoding='utf-8') as f:
        pos =f.readlines()
    with open("情感词典\\负面情绪词.txt", "r",encoding='utf-8') as f:
        neg = f.readlines()
    with open("情感词典\\否定词.txt","r",encoding='utf-8') as f:
        not_word =f.readlines()


    with open(file_path,"r") as f:
        lines=f.readlines()

    with open(target_path, "w") as f:

        for line in lines:


            if(line=='\n'):
                f.write('\n')

                continue

            l = line.split()
            value = 0
            count = 0
            rate = []

            for i in l:    #一直累计情绪词前面的副词与否定词，直到遇情绪为止
                if (i in most):
                    rate.append(2)
                elif (isHit(i,not_word)):
                    count += 1
                elif (i in more):
                    rate.append(1.2)
                elif (i in very):
                    rate.append(1.25)
                elif (i in little):
                    rate.append(0.8)
                elif (i in insufficiently):
                    rate.append(0.5)
                elif (isHit(i,pos)):    #根据副词加权，否定词数量取反
                    num = 1
                    for j in rate:
                        num = num * j
                    rate = []

                    if (count % 2 == 1):
                        num = 0.0-num
                        count = 0

                    value += num
                elif (isHit(i,neg)):
                    num = 1
                    for j in rate:
                        num = num * j
                    rate = []

                    if (count % 2 == 1):
                        num = 0.0-num
                        count = 0

                    value -= num



            f.write(str(value))
            f.write('\n')






def isHit(word,lines):
    for line in lines:
        l=line.split()
        for i in l:
            if word==i :
                return True

    return False






def findTheEmotion(file_path,target_path):
    stop_word_path = "情感词典\\chineseStopWords.txt"
    with open("情感词典\\正面情绪词.txt","r",encoding='utf-8') as f:
        pos =f.readlines()
    with open("情感词典\\负面情绪词.txt", "r",encoding='utf-8') as f:
        neg = f.readlines()
    with open(file_path,"r") as f:
        lines=f.readlines()
    with open(stop_word_path, "r") as stop:
        r = stop.read()

    with open(target_path, "w") as file:
        for line in lines:
            l = line.split()
            for i in l:
                if (isHit(i,pos) or isHit(i,neg)):
                    if (i not in r):
                        file.write(i + " ")

            file.write('\n')


def reCluEmotionalValue(first_value_path,weight_value_path,target_path):
    isHead=True

    head=""

    with open(target_path,"w") as file:

        with open(weight_value_path, "r") as w:
            weightValue = w.readline()

            with open(first_value_path, "r") as f:
                lines = f.readlines()

                for line in lines:
                    if (line == '\n'):
                        file.write("\n")
                        weightValue=w.readline()
                        isHead = True  #下一条是微博内容
                        continue

                    l = line.split()
                    for i in l:
                        if (isHead):
                            head = i
                            isHead = False
                            continue

                        if (float(head) * float(i) >= 0):  #微博内容情绪与评论相同，对评论情感加强
                            temp = float(weightValue) * float(i)
                            file.write(str(temp) + '\n')
                        else: #两者相反，对评论情感进行削弱
                            temp = float(i) / float(weightValue)
                            file.write(str(temp) + '\n')


def cluISO(file_path,target_path):
    with open(file_path,"r") as f:
        lines=f.readlines()
    min=findMin(lines)
    max=findMax(lines)
    with open(target_path,"w") as t:
        for line in lines:
            l = line.split()
            for i in l:
                value = float(i)
                if (value > 0):
                    value=value/max

                elif (value<0):
                    value=value/min
                    value=0.0-value  #为了方便计算，将ISO分正负

                else:
                    value=0

                t.write(str(value)+'\n')






def findMax(lines):
    max=0
    for line in lines:
        l=line.split()
        for i in l:
            if(float(i)>max):
                max=float(i)
    return max

def findMin(lines):
    min=0
    for line in lines:
        l=line.split()
        for i in l:
            if(float(i)<min):
                min=float(i)
    return min


def cluVector(comment_and_ISO_path,frequency_and_TFIDF_path,target_path):
    with open("情感词典\\正面情绪词.txt","r",encoding='utf-8') as f:
        pos =f.readlines()
    with open("情感词典\\负面情绪词.txt", "r",encoding='utf-8') as f:
        neg = f.readlines()

    with open(comment_and_ISO_path, 'r', newline='') as csvfile1:
        comment_and_ISO = csv.DictReader(csvfile1)

        with open(target_path, "w") as file:

            for pair2 in comment_and_ISO:

                with open(frequency_and_TFIDF_path, 'r', newline='') as csvfile2:
                    frequency_and_TFIDF = csv.DictReader(csvfile2)

                    for pair1 in frequency_and_TFIDF:
                        comment = pair2['评论'].split()
                        isWrite = False

                        for i in comment:
                            isPos = False
                            isNeg = False

                            if (i == pair1['高频词']):
                                isWrite = True
                                isPos = isHit(pair1['高频词'], pos)
                                isNeg = isHit(pair1['高频词'], neg)
                                ISO = float(pair2['ISO'])
                                TF_IDF = float(pair1['TF-IDF'])

                                if isPos:

                                    if (ISO > 0):
                                        num = (1.0 + ISO) * TF_IDF
                                    else:
                                        num = TF_IDF
                                elif isNeg:

                                    if (ISO < 0):    #由于计算ISO的时候将数据分为了正负，故最后向量计算需考虑ISO的正负
                                        ISO = 0.0-ISO
                                        num = (1 + ISO) * TF_IDF
                                        num = 0.0-num
                                    else:
                                        num = 0.0-TF_IDF

                                else:
                                    num = TF_IDF

                                file.write(str(num) + " ")
                                break

                        if not isWrite:
                            file.write("0 ")

                    file.write('\n')




def combineCommentAndISOToCSV(comment_path,ISO_path,csv_path):

    with open(csv_path, 'w', newline='') as csvfile:
        name = ["评论","ISO"]
        writer = csv.DictWriter(csvfile, fieldnames=name)

        # 在Excel第一行写入字段名
        writer.writeheader()
        file1=open(comment_path,"r")
        lines=file1.readlines()
        file2=open(ISO_path,"r")

        dict = {}
        for line in lines:
            dict["评论"] = line
            dict['ISO']=file2.readline().replace("\n","")
            writer.writerow(dict)
        file2.close()
        file1.close()


def filterTextAndLine(file_path,target_path):
    with open(file_path,"r") as f:
        lines=f.readlines()


    with open(target_path,"w") as f:
        isHead=True
        for line in lines:
            if isHead:
                isHead=False
                continue

            if (line == '\n'):
                isHead = True
                continue

            f.write(line)


def takeCommentAndVector(comment_ISO_path,vector_path,target_path):
    with open(comment_ISO_path, 'r', newline='') as csvFile:
        reader = csv.DictReader(csvFile)

        with open(target_path,'w', newline='') as targetFile:
            name=['评论','向量']
            writer = csv.DictWriter(targetFile, fieldnames=name)

            # 在Excel第一行写入字段名
            writer.writeheader()

            # 写入每一行的数据
            dict = {}

            file=open(vector_path,"r")
            line=file.readline()

            for i in reader:
                dict['评论']=i['评论']
                dict['向量']=line.replace("\n","")

                writer.writerow(dict)

                line=file.readline()

            file.close()


def whichType(file_path):
    countPos=0
    countNeg=0
    countZero=0
    with open(file_path,"r") as f:
        lines=f.readlines()
    for line in lines:
        if(line=='\n'):
            continue
        l=line.split()
        for i in l:
            num=float(i)
            if(num>0):
                countPos+=1
            elif(num<0):
                countNeg+=1
            else:
                countZero+=1

    print("中性",countZero)
    print("正面",countPos)
    print("负面",countNeg)




if __name__=='__main__':

    for i in range(1,5):
        # 下列函数的最后一个形参地址都是存储结果的地址
        cutByJieba("原始数据_时期"+str(i)+".txt","时期"+str(i)+".txt")
        findTheKeyword("时期"+str(i)+".txt", "高频"+str(i)+".csv", 50, 1)

        culEmotionalValue("时期"+str(i)+".txt","情感值"+str(i)+".txt")
        reCluEmotionalValue("情感值"+str(i)+".txt", "权值"+str(i)+".txt",
              "二次加权结果"+str(i)+".txt")  #二次加权

        filterTextAndLine("时期" + str(i) + ".txt", "temp_comment.txt")

        cluISO("二次加权结果" + str(i) + ".txt", "temp_ISO.txt")

        combineCommentAndISOToCSV("temp_comment.txt", "temp_ISO.txt",
                                  "comment_ISO_" + str(i) + ".csv")

        cluVector("comment_ISO_" + str(i) + ".csv",
                  "高频" + str(i) + ".csv",
                  "time0" + str(i) + ".txt")

        takeCommentAndVector("comment_ISO_" + str(i) + ".csv",
                             "time0" + str(i) + ".txt",
                             "comment_vector_"+str(i)+".csv")



    for i in range(1,5):
        findTheEmotion("时期"+str(i)+".txt","前50高频情绪\\temp.txt")
        findTheKeyword("temp.txt",
                       "emotional_words_"+str(i)+".csv",50,1)

    #下列程序仅用于辅助分析实验结果的情感倾向，并没有参与中间的数据处理
    # for i in range(1,5):
    #     print("time0"+str(i))
    #     for j in range(1,4):
    #         print("category_0" + str(j))
    #         culEmotionalValue("D:\\评论分类结果\\time01_comment_category_0" + str(j) + ".txt", "D:\\评论分类结果\\temp.txt")
    #         whichType("D:\\评论分类结果\\temp.txt")
    #     print()

    # with open("C:\\Users\\叶俊濠\\Desktop\\高频1.csv", 'r', newline='') as csvfile:  # 参数 newline=''不能动，直接用就行
    #     reader = csv.DictReader(csvfile)
    #     for row in reader:
    #         # 每一行是一个 dict 对象 {key：value}
    #         print(row['TF-IDF'])