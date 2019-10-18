# encoding = utf-8
__author__ = "Ang Li"

line_count = 1
page_count = 1
page_name = 'kernel-list_' + str(page_count) + '.txt'

with open('kernel-use.list','r',encoding='utf-8') as f:
    while True:
        for line in f:
            if line_count == 10:
                line = line.strip()

            if line_count == 11:
                line_count = 1
                page_count += 1
                page_name = 'kernel-list_' + str(page_count) + '.txt'
                print(page_name)

            with open(page_name,'a+',encoding='utf-8') as w:
                w.write(line)

            line_count += 1

exit()
