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

with open("pickle-test.txt","rb") as f:
    data = pickle.loads(f.read())
    print(data["func"]("li"))


#with open("pickle-test.txt","wb") as f:
#    f.write(pickle.dumps(info))
