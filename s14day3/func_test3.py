# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com

# def test(*args):
#     print(args)
#
# test(1,2,3,24,3)





def change_name():
    name = ['A','B','C','D']
    name[0] = "X"
    print("in func",name)
change_name()



def calc(n):
    print(n)
    return calc(n+1)
calc(1)