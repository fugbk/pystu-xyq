# encoding = utf-8
__author__ = "Ang Li"

# assert

list = [1,2,3]

assert len(list) == 3

def student(name,age,sex):
    assert type(name) is str
    assert type(age) is int
    assert type(sex) is str

student("Tom","21","M")
