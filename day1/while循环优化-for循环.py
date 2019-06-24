# Author：Li Ang
# encoding=utf8
'''
for i in range(5):      #range(5) 相当于0,1,2,3,4，
    print("loop",i)
'''

'''
age = 20
for i in range(3):
    guess_age = int(input("guess_age:"))
    print("time",i)
    if guess_age == age:
        print("Yes, you got it...",guess_age)
    elif guess_age > age:
        print("No, think bigger!",guess_age)
    else:
        print("No, think smaller",guess_age)
else:
    print("Sorry , you have tired too many times.. fuck off")

'''

'''
#continue  跳出本次循环
for i in range(0,5):
    if i < 3:
        print("loop",i)
    else:
        print("haha...")
        continue
        print("hehe...")
'''

#break 结束整个循环
for i in range(5):
    if i < 3:
        print("Loop",i)
    else:
        print("hehe...")
        break
        print("haha...")
