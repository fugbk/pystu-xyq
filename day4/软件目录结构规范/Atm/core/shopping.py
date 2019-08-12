# Author：Li Ang
# encoding=utf8
#购物车程序
import json
import os
import random
import string
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from bin import atm

cost_history_log = os.path.join(BASE_DIR,"log","cost_history.log")
product_list = [
    ('iphone',7000),
    ('mac',17000),
    ('book',10),
    ('watch',300)
]
user,passwd = "ali","123"

def auth(func):
    def wrapper(*args,**kwargs):
        username = str(input("Ple Enter Your shopping name>>> "))
        password = input("Ple Enter Your passwd for {} >>> ".format(username))
        if username == user and password == passwd:
            print("Authorized Successd！\n Welcome to shopping Word!\n")
            return func(*args,**kwargs)
        else:
            print("Sorry, Authorized failed.")
            return "auth failed on mode"
    return wrapper

def cost_colse(user,shopping_list,cost_pice):
    print(user,"cost pice is ",cost_pice)
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    id = "s" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + salt
    cost_list = {
        "time":time.strftime("%Y-%m-%d", time.localtime()),
        "user":user,
        "shopping_list":shopping_list,
        "cost":cost_pice,
        "cost_id":id
    }
    with open(cost_history_log,"a+") as f:
        json.dump(cost_list,f)
        f.write("\n")
    print("Just a moment, please")
    atm.js(cost_pice,id)
    return cost_pice,id

@auth
def shopping():
    choice_pice = 0
    shopping_list = []
    while True:
        print("---------shopping list---------")
        for index,item in enumerate(product_list):
            print(index,item)
        print("--------------------------")
        choice = input("your choice:")
        if choice == "q":
            if choice_pice == 0:
                print("goodby")
                exit()
            else:
                return cost_colse(user,shopping_list,choice_pice)

        choice = int(choice)
        if choice < len(product_list) and choice >= 0:
            choice_pice += int(product_list[choice][1])
            shopping_list.append(product_list[choice])
            print("your shopping cost is \033[0;31m%s\033[0m" %(choice_pice))
            print("your shopping list is",shopping_list,"\n")
        else:
            print("Please input your choice 0 -",len(product_list)-1,"\n")

if __name__ == "__main__":
    shopping()