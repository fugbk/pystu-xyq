# Author：Li Ang
# encoding=utf8

age = 23
count = 0
enable = 3
while count < enable:
    guess_age = int(input("guess_age:"))
    if guess_age == age:
       print("Yes ,you got it...")
       break
    elif guess_age > age:
       print("No,think bigger!")
    else:
        print("No,think smaller!")
    count +=1
    if count == 3:             #如果输出三次，count = 3则提示是否继续，如果输入n则退出循环，非 则清空计数器，重新执行。
        countine_confirm = input("Do you want to keep guessing...?")
        if countine_confirm != 'n':
            count = 0

#else:
#    print("you have tired too many times.. fuck off")
'''


age = 23
count = 0
enable = 3
while count < enable:
    guess_age = int(input("guess_age:"))
    if guess_age == age:
       print("Yes ,you got it...")
       break
    elif guess_age > age:
       print("No,think bigger!")
    else:
        print("No,think smaller!")
    count +=1
else:
    print("you have tired too many times.. fuck off")

'''