# encoding = utf-8
__author__ = "Ang Li"

import shelve
d = shelve.open("shelve.txt")  # 打开一个文件

name = "Tom"
age = 24
student_info = ["sdkj", "20140708", "信息工程", "14届", ]
friends = {
    "Jerry": "man",
    "Marry": "woman",
}


d["name"] = name
d["school"] = student_info
d["friends"] = friends

d.close()


