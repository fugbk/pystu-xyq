# encoding = utf-8
__author__ = "Ang Li"

line_count = 1
page_count = 1

with open('kernel-use.list','r',encoding='utf-8') as f:
    while True:
        page_name = 'kernel-list_' + str(page_count) + '.txt'
        if line_count == 10:
            line_count = 0
        else:
            line_count += 1
        for line in f:
            with open(page_name,'a+',encoding='utf-8') as w:
                w.write(line)
                w.write("\n")
        page_count += 1