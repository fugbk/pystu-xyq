# encoding = utf-8
__author__ = "Ang Li"

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(object,self.name)

s = Student("Tom",22)
s()

Student("Jerry",21)()


 
