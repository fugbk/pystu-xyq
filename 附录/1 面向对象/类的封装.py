# encoding = utf-8
__author__ = "Ang Li"

class Person:
    def __init__(self):
        self.attack_val = 10
        self.__life_val = 100       # 变量前加上__表示私有变量，只能类中调用；
    def get_life_var(self):
        print("血量为",self.__life_val)
    def __breath(self):     # 方法前加上__表示为私有方法，只能在类中调用；
        print("正在呼吸...")
    def got_attack(self):
        self.__life_val -= self.attack_val
        print("收到攻击，掉血 %s, 剩余血量 %s" %(self.attack_val,self.__life_val))
        self.__breath()

p = Person()
p.get_life_var()
p.got_attack()
print("---------------")
p._Person__breath()        # 调用方法：实例名称._类名称+方法名称()