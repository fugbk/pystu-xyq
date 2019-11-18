# encoding = utf-8
__author__ = "Ang Li"


import random

def verification_code():
    """
    生产字母和数字组合的四位随机验证码
    """
    check_code = ""
    for i in range(4):
        current = random.randint(0, 3)
        if i == current:
            temp = chr(random.randint(65, 90))  # 65-90 表示ASCII 中的A-Z, chr() 转换成ASCII码
        else:
            temp = random.randint(0,9)
        check_code += str(temp)

    print(check_code)

if __name__ == '__main__':
    verification_code()






