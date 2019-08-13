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



def repayment(user):
    repay = int(input("repayment mooney:"))
    with open(balance_out_file,"r") as f:
        balance_list = json.load(f)
        balance_list[user] += repay
    with open(balance_out_file,"w+") as f:
        json.dump(balance_list,f)
    balance_mooney = balance_list[user]
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 4))
    event_id = "s" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + salt
    sum = "+" + str(repay)
    info = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "user": user,
        "type": "repayment",
        "cost": sum,
        "balance": balance_mooney,
        "des": "repayment",
        "event_id": event_id
    }
    with open(balance_log, "a+") as f:
        json.dump(info,f)
        f.write("\n")
    print("Repayment Succeed.\nYour balance mooney is %s" %(balance_mooney))

def main():
    pass

if __name__ == "__main__":
    main()