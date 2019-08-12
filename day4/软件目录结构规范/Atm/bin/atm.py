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

balance_out_file = os.path.join(BASE_DIR, "conf", "balance_outstanding.txt")
balance_log = os.path.join(BASE_DIR, "log", "balance.log")
users_list = os.path.join(BASE_DIR,"conf","atm_users.list")

with open(users_list,"r") as f:
    user_list = json.load(f)

def auths(func):
    def wrapper(*args,**kwargs):
        user_name = input("user name: ")
        user_passwd = input("user passwd: ")
        if user_name in user_list:
            if user_passwd == str(user_list[user_name]):
                print("Authorized succeed，WelCome %s login Atm" %(user_name))
                func(*args,**kwargs,user=user_name)
            else:
                print("Authorized Failed !")
                exit()
        else:
            print("User %s are not exist" %(user_name))
            exit()
    return wrapper

@auths
def js(cost_price, cost_id, **kwargs):
    login_user = kwargs["user"]
    with open(balance_out_file, "r+") as f:
        balance_list = json.load(f)
        user_balance = balance_list[login_user]
    if user_balance < cost_price:
        print("not enough mooney")
        exit()
    else:
        last_balance = user_balance - cost_price * 1.05
        balance_list[login_user] = last_balance

    with open(balance_out_file, "w+") as f:
        json.dump(balance_list,f)
    print("balance mooney is",last_balance)
    time_strip = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    id = "a" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + salt

    log_info = {
        "time":time_strip,
        "user":login_user,
        "cost":-cost_price,
        "balance":last_balance,
        "type":"internet payment",
        "id":id,
        "des":cost_id
    }

    with open(balance_log, "a+") as f:
        json.dump(log_info,f)
        f.write("\n")

#js(200,"fhsjddkahj")

def main():
    pass

if __name__ == "__main__":
    main()