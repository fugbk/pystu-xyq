# encoding = utf-8
__author__ = "Ang Li"

import os
import sys

# 导入../../core/main.py
# 1. 获取当前项目的绝对路径
print(os.path.abspath(__file__))    #当前文件 atm.py 的绝对路径
print(os.path.dirname(os.path.abspath(__file__)))   # 当前文件的父目录 bin/ 的绝对路径
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #当前文件的父目录 的 父目录 的绝对路径 ---也就是
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前项目的绝对路径

# 2. 将当前项目的绝对路径，加入sys.path 环境变量
sys.path.append(BASE_DIR)

# 3. 导入 core 下的程序

from core import main

main.login()