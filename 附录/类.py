# encoding = utf-8
__author__ = "Ang Li"

class Animal:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eating(self):
        print("%s is eating..." % self.name)

class Person(Animal):
    def __init__(self,name,age,sex,hobbie):  # 保护原本父类的参数，和新增的子类的参数
        # Animal.__init__(self,name,age,sex)   # 方法一、父类的参数，传入父类的变量
        # super(Person, self).__init__(name,age,sex)   # 方法二、常用这种，效果同上
        super().__init__(name,age,sex)   # 方法三、效果同上
        self.hobbie = hobbie    # 新增的 属性

    def eating(self):
        Animal.eating(self)
        print("%s are not eat..." % self.name)

p1 = Person("Alex",22,"M","game")

print(p1.name,p1.age,p1.hobbie)




 
