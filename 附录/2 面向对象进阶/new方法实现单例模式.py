# encoding = utf-8
__author__ = "Ang Li"
import datetime
import time


class Printer(object):
    task_list = []
    instance = None
    def __init__(self,name):
        self.now_time = datetime.datetime.now()
        self.name = name
        print("生成打印机[%s]" %name)
        print("这是init 的时间",self.now_time)
    def add_task(self,job):
        self.task_list.append(job) # 把打印任务添加到这个列表
        print("%s 添加了一个任务  %s 到打印机，总任务数 %s" %(self.name,job,len(self.task_list)))

    def __new__(cls, *args, **kwargs):
        print("cls instance",cls.instance)
        if cls.instance is None: # 如果是第一个实例
            print(args,kwargs)
            obj = object.__new__(cls) # 则进行实例化
            cls.instance = obj # 把实例化的对象保存下来
            print("-----cls instance", cls.instance)
            return cls.instance  # 以后没次实例化
        else:
            print(p1.instance.name)
            return cls.instance # 以后没次实例化

p1 = Printer("pdf")
#print(p1,p1.name)
#p1.add_task("pdf print")
print("---------------------")

time.sleep(3)

p2 = Printer("word")
#print(p2,p2.name)
#p2.add_task("word print")
print("---------------------")

#print(p1.now_time,p2.now_time)

p3 = Printer("excel")

# print("%s\n%s" %(p1,p2))
# print(p1.name,p2.name)
#
# #p1.add_task("pdf print")
# # p2.add_task("word print")
# # p3.add_task("excel print")
#
# print("%s" %(p1))