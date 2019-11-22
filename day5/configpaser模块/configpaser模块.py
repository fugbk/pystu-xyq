# encoding = utf-8
__author__ = "Ang Li"

import configparser

conf = configparser.ConfigParser()   # 先生成一个configpaser的对象

# conf.read("my2.cnf", encoding="utf-8")   # 读取配置文件

conf["user"] = {}
conf["user"]["name"] = "Tom"
conf["user"]["password"] = "123456"

conf["client"] = {}
conf["client"]["ip"] = "192.168.56.1"
conf["client"]["hostname"] = "Tmp"

conf["server"] = {}
conf["server"]["server-id"] = "1"

conf["backup"] = {
    "back-type": "logger back",
    "unzip": "YES",
    "logger-server": "192.168.100.1"
}

with open("my3.txt", "w") as configfile:
    conf.write(configfile)



# print(conf.sections())   # 输出所有节点
#
# print(conf['client']["port"])  # 获取某一具体配置
#
#
# for key in conf['client']:
#     print(key)
#
#
# conf.remove_section['mysql']["server-id"]
# conf.write(open('my.cnf', 'w'))

conf["backup"]["unzip"] = "No"
conf.write(open("my3.txt", "w"))
