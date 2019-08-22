# encoding = utf-8
__author__ = "Ang Li"

class Dog:
    def sound(self):
        print("汪汪汪。。。")

class Cat:
    def sound(self):
        print("喵喵喵。。。")

def make_sound(animal_object):
    animal_object.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)