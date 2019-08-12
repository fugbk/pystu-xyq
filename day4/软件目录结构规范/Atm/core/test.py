# encoding = utf-8
__author__ = "Ang Li"
import json

import shopping

print(shopping.cost_history_log)

with open(shopping.cost_history_log,"r") as f:
    for line in f.readlines():
        data = json.loads(line)
        print(data["cost_id"])
