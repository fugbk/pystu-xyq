# encoding = utf-8
__author__ = "Ang Li"

class Printer(object):
    task_list = []
    instance = None
    def __init__(self,name):
        self.name = name
        print("生成打印机[%s]" %name)

    def add_task(self,job):
        self.task_list.append(job)
        print("%s 添加了任务 %s" %(self.name,job))

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            obj = object.__new__(cls)
            cls.instance = obj
            print(obj)



p1 = Printer("pdf")
p2 = Printer("word")
p3 = Printer("excel")

p1.add_task("pdf print")
p2.add_task("word print")
p3.add_task("excel print")

print("%s\n%s\n%s" %(p1,p2,p3))