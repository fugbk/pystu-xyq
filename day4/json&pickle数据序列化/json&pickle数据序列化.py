# encoding = utf-8
__author__ = "Ang Li"

def cut_off():
    cut_off_flog = "*"
    print(cut_off_flog.ljust(70, '*'))


info = {
    "age":20,
    "sex":"man",
    "color":"red"
}

with open("test.txt","w+") as f:
    f.write(str(info))

with open("test.txt","r") as f:
    data = eval(f.read())

    print(data["age"])