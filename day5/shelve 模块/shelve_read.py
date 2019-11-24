# encoding = utf-8
__author__ = "Ang Li"

import shelve

d = shelve.open("shelve.txt")
# print(d.get("name"))
# print(d.get("school"))
# print(d.get("friends"))

for k, v in d.items():
    print(k, v)


