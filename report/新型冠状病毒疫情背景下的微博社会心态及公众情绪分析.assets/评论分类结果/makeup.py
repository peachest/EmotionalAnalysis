def txtToHtml(filename):
    frompath = filename + ".txt"
    topath = filename+ ".html"
    txt = open(frompath, "r")
    html = open(topath, "w", encoding='utf-8')

    message = "<html><body><head><meta charset = 'utf-8'>" \
              "<title></title></head>"
    lines = txt.readlines()
    for line in lines:
        message += line + "<br/>"
        pass
    message += "</body></html>"

    html.write(message)
    txt.close()
    html.close()

    pass

if (__name__ == "__main__"):
    # for i in range(1, 5):
    #     for j in range(1, 4):
    #         filename = "time0{}_comment_category_0{}".format(i, j)
    #         txtToHtml(filename)
    for j in range(1, 5):
        filename = "time04_comment_category_0{}(k=4)".format(j)
        txtToHtml(filename)
    pass