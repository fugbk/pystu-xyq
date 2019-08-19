# encoding = utf-8
__author__ = "Ang Li"


class Dog:  # 类
    life_val = 100  # 类属性，类变量 ，类中的对象共享
    attack_val = 30

    def __init__(self, name, age):  # 初始函数，构造函数 定义每个实例的私有属性，存储在对象的内存空间中
        self.name = name  # 实例创建时，会执行这个函数
        self.age = age  # 将实例与属性绑定起来

    def say_hi(self):  # 方法
        print("I'm a dog, My name is %s and my age is %s." % (self.name, self.age))
        print(self.name, self.life_val, self.attack_val)


d1 = Dog("Tom", 3)
d2 = Dog("Jerry", 2)

d1.life_val = 200
print(d1.life_val)

Dog.life_val = 200  # 可以通过 【类名称】.【属性】 的方式 修改公共属性

d1.age = 100  # 实例可以修改初始化的属性，因为这些事存在实例自己的内存空间中的
print(d1.age)
d1.say_hi()
d2.say_hi()

d3 = Dog("ang", 4)
print(d3.life_val)