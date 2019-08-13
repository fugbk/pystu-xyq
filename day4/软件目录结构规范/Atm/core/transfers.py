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


def transfer(user):
    s_user = user
    while True:
        flag = input("Type q to quit >>>")
        if flag == "q":
            return 0
        else:
            with open(balance_out_file,"r") as f:
                price_list = json.load(f)
                d_user = input("Reciprocal Account >>> ")
            if d_user not in price_list:
                print("Sorry, reciprocal account are not exist.")
                exit()

            s_user_price, d_user_price= price_list[s_user], price_list[d_user]
            print("Your balance mooney is",s_user_price)
            price = int(input("Price >>>"))
            if s_user_price < price:
                print("Sorry, you not have enough mooney!")
                exit()
            control = input("Please confirm whether to transfer the money [y|n]:")
            if control == "n":
                continue
            elif control == "y":
                price_list[s_user] = s_user_price - price
                price_list[d_user] = d_user_price + price
                with open(balance_out_file,"w") as f:
                    json.dump(price_list, f)
                print("Transfer Succeed!\nNow your balance is ",price_list[s_user])
                salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
                id = "t" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + salt
                foo = "transfer to " + d_user
                log_info = {
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "user": s_user,
                    "cost": -price,
                    "balance": price_list[s_user],
                    "type": "transfer",
                    "id": id,
                    "des": foo
                }

                foo = s_user + " to transfer"
                bar = "+" + str(price)
                log_info_d = {
                    "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "user": d_user,
                    "cost": bar,
                    "balance": price_list[d_user],
                    "type": "transfer",
                    "id": id,
                    "des": foo
                }
                with open(balance_log, "a+") as f:
                    json.dump(log_info, f)
                    f.write("\n")
                    json.dump(log_info_d, f)
                    f.write("\n")


def main():
    pass
if __name__ == "__main__":
    main()