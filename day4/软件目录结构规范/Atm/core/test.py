# encoding = utf-8
__author__ = "Ang Li"
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

cost_history_log = os.path.join(BASE_DIR, "log", "shopping_history.log")
product_lists = os.path.join(BASE_DIR,"conf","product_price.list")

product_list = [
    ('iphone', 7000),
    ('mac', 17000),
    ('book', 10),
    ('watch', 300)
]
with open(product_lists,"w+") as f:
    json.dump(product_list,f)