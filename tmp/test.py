# encoding = utf-8
__author__ = "Ang Li"

for i in range(1,1):
    print(i)

word = "attacd"
print(word.find("t"))

l = [1,23,4,5]
print(l)

l[l.index(1)] = "c"
print(l)


a = "Yesterday, the moon was blue,"

print(a.replace(",","").split())

print(id(word))

def test():
    local_ver = 32
print(locals())

test()


a = {1:2,2:3,3:4,4:5,-1:-2,-3:23}

print(sorted(a.items(),key= lambda x:x[1]))
print(a)


a = [x for x in range(4)]
b = [x for x in range(-7,1)]
for i in zip(a,b):
    print(i)

