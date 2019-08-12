# encoding = utf-8
__author__ = "Ang Li"

import json
import os
import random
import string
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

blance_out_file = os.path.join(BASE_DIR,"conf","blance_outstanding.txt")
blance_log = os.path.join(BASE_DIR,"log","blance.log")

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
    with open(blance_out_file,"r+") as f:
        blance_list = json.load(f)
        user_blance = blance_list[login_user]
    if user_blance < cost_pice:
        print("not enough mooney")
        exit()
    else:
        laset_balance = user_blance - cost_pice * 1.05
        blance_list[login_user] = laset_balance

    with open(blance_out_file,"w+") as f:
        json.dump(blance_list,f)
    print("balance mooney is",laset_balance)
    time_strip = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    id = "a" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + salt

    log_info = {
        "time":time_strip,
        "user":login_user,
        "cost":cost_pice,
        "blance":laset_balance,
        "id":id,
        "des":cost_id
    }

    with open(blance_log,"a+") as f:
        json.dump(log_info,f)
        f.write("\n")

def main():
    pass

if __name__ == "__main__":
    main()