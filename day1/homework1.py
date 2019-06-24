# Author：Li Ang
# encoding=utf8
'''
编写登陆接口
1.输入用户名和密码；
2.认证成功后显示欢迎信息；
3.输错三次后锁定账户，进程重启后也不允许继续登录。
'''



source = open(r'C:\Users\ali61\OneDrive\python\python笔记\user.txt')
_user = source.readline()
source2 = open(r'C:\Users\ali61\OneDrive\python\python笔记\passwd.txt')
_passwd = source2.readline()

#source3 = open("C:\Users\ali61\OneDrive\python\python笔记\user.txt", "w+")

count = 0
while count < 3:
    user = input("Username:")
    passwd = input("Password:")
    for line in source.readline():
        if user == line:
            print("Sorry,Your account has been locked, please contact the administrator ")
            break
    if user == _user and passwd == _passwd:
        print("Hello ,wellcome {_user} login...".format(_user=user))
        break
    else:
        count += 1
        print("user or passwd error...")
        if count == 3:
            print("you have tried too mang times...fuck off")
            enable = input("Do you want to keep guessing?")
            if enable == "n":
                count = 0
#            source.writelines(user)
source.close()
source2.close()

