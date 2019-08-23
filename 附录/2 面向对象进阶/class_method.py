# encoding = utf-8
__author__ = "Ang Li"


# class Student(object):
#     __stu_num = 0
#     def __init__(self,name):
#         self.name = name
#         Student.__stu_num += 1
#         print("加入了一个学生 ",self.name,Student.__stu_num)
#
#
# s1 = Student("Tom")
# s2 = Student("Alex")
# s3 = Student("jerry")


class Student(object):
    __stu_num = 0
    def __init__(self,name):
        self.name = name
        self.add_stu(self)
        #print("加入了一个学生 ",self.name,Student.__stu_num)

    @classmethod
    def add_stu(cls,obj):
        if obj.name:
            cls.__stu_num += 1
            print("添加了一个学生" ,cls.__stu_num)
        else:
            print("error")


s1 = Student("Tom")
s2 = Student("Alex")
s3 = Student("jerry")
