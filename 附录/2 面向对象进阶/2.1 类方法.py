# encoding = utf-8
__author__ = "Ang Li"

class Dog(object):
    name = "Alex" # 定义类变量
    def __init__(self,name):
        self.name = name # 定义实例变量

    @classmethod
    def eat(self):
        print("eat ---> %s" % self) # eat ---> <class '__main__.Dog'> # 打印的是类本身
        print("Dog %s is eating..." % self.name) # self 先找实例变量,实例变量找不到再找类变量

    def sleep(self):
        print("sleep ---> %s" % self) # sleep ---> <__main__.Dog object at 0x00000217D086CDC8> 打印Dog这个对象
        print("Dog %s is sleeping..." %(self.name))


d = Dog("Tom")
d.eat()
d.sleep()

