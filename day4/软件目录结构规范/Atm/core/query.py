# encoding = utf-8
__author__ = "Ang Li"

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

balance_out_file = os.path.join(BASE_DIR, "conf", "balance_outstanding.txt")


def query(user):
    login_user = user
    with open(balance_out_file,"r") as f:
        balance_list = json.load(f)
        print("Your balance is ",balance_list[login_user])
        return 0

if __name__ == "__main__":
    query()