# encoding = utf-8
__author__ = "Ang Li"

#Author：LiAng
#encoding=utf8
# import getpass
# username = input("Username:")
# password = getpass.getpass("Password:")
# print(username,password)

user_list = {
    "ali":123,
    "tom":234,
    "jerry":"qwer"
}

def auths(func):
    def wrapper(*args,**kwargs):
        user_name = input("user name: ")
        user_passwd = input("user passwd: ")
        if user_name in user_list:
            if user_passwd == str(user_list[user_name]):
                print("Authorized successd，WelCome %s login Atm" %(user_name))
                func(*args,**kwargs,user=user_name)
            else:
                print("Authorized Failed !")
                exit()
        else:
            print("User %s are not exist" %(user_name))
            exit()
    return wrapper


@auths
def js(cost_pice,cost_id,**kwargs):
    login_user = kwargs["user"]
    print(login_user)
    # with open(blance_out_file,"r+") as f:
    #     blance_dir = json.load(f)
    #     user_balance = blance_dir[login_user]
    #     print(user_balance)

js(100,78678678)
