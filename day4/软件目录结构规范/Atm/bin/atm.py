# encoding = utf-8
__author__ = "Ang Li"

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

balance_out_file = os.path.join(BASE_DIR, "conf", "balance_outstanding.txt")
balance_log = os.path.join(BASE_DIR, "log", "balance.log")
users_list = os.path.join(BASE_DIR,"conf","atm_users.list")

from core import transfers

with open(users_list,"r") as f:
    user_list = json.load(f)

def auths(func):
    def wrapper(*args,**kwargs):
        print("Welcome login ATM, please input your authentic key")
        user_name = input("user name: ")
        user_passwd = input("user passwd: ")
        if user_name in user_list:
            if user_passwd == str(user_list[user_name]):
                print("Authorized succeed，WelCome %s" %(user_name))
                func(*args,**kwargs,user_name=user_name)
            else:
                print("Authorized Failed !")
                exit()
        else:
            print("User %s are not exist" %(user_name))
            exit()
    return wrapper

def exit(func):
    def warpper(*args,**kwargs):
        func(*args,**kwargs)
        contorl = input("Type 'q' to quit >>>")
        if contorl == "q":
            return "quit"
    return warpper

def user_manager():
    print("user manager module.")

def atm_log(user):
    print("atm log module.")
    print(user)

def repayment(user):
    print("repayment module.")
    print(user)

def transfer(user):
    print("transfer module.")


def query():
    print("query module.")

@auths
def control(user_name):
    flag = True
    task_list = [
        "Query",
        "Transfers",
        "Repayment",
        "Atm Log",
        "User Manager",
    ]

    while flag:
        print("What are your want to do ?")
        for item,index in enumerate(task_list):
            print("\t", item, " ", index)
        choice = input("Ple Enter Your Choice, type q to quit: ")

        if choice == "q":
            flag = False
        elif int(choice) >= len(task_list):
            print("Input Error, your choice must smaller than %s, please try again." %(len(task_list)))
            continue
        elif choice == "0":
            query()
        elif choice == "1":
            transfers.transfer(user=user_name)
        elif choice == "2":
            repayment(user_name)
        elif choice == "3":
            atm_log(user_name)
        elif choice == "4":
            user_manager()
        else:
            print("Syntax error.")
            flag = False
control()


