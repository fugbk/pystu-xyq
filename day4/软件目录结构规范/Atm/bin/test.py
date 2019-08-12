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
user_list = {
    "ali":123,
    "tom":234,
    "jerry":"qwer"
}
with open(users_list,"w+") as f:
    json.dump(user_list,f)
 
