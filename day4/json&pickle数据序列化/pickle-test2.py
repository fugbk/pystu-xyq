# encoding = utf-8
__author__ = "Ang Li"


def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


import pickle

def name(name):
    print("My name is",name)
info = {
    "age":20,
    "sex":"man",
    "color":"red",
    "func":name
}

with open("pickle-test.txt","wb") as f:
    pickle.dump(info,f)

with open("pickle-test.txt","rb") as f:
    data = pickle.load(f)
    print(data["func"]("li"))



