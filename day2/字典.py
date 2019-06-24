# Author：Li Ang
# encoding=utf8
'''
info = {
    'stu1101': "zhangshan",
    'stu1102': "LiShi",
    'stu1103': "Wang",
}

print(info)

print(info["stu1101"])
info["sty1101"] = "ZHANG"  #增加key

print(info["sty1101"])

#info.pop("sty1101")  #删除
del info["sty1101"]    #删除

print(info.get("sty1101"))   #获取，不存在 不会报错

print("stu1101" in info)     #检查key 是否在字典里，  info.has_key('1101') py2.X
'''


'''
#多级字典嵌套及操作
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
#字典-字典-列表
av_catalog["大陆"]["1024"][1] = "可以做国内镜像"      #直接修改，若key不存在 则会 添加
print(av_catalog["大陆"])

av_catalog.setdefault("台湾",{"www.baidu.com":[1,2]})       #.setdefault 添加时会检查，key 是否存在，若存在则不会添加

print(av_catalog["台湾"])
'''


#.update  合并字典，有交叉的则合并，没有交叉的 新创建
a = {
    "stu1101": "Wang",
    "stu1102": "Li",
    "stu1103": "Zhang"
}

b = {
    "stu1101": "Alex",
    1:2,
    3:5
}

a.update(b)
print(a)
#OUTPUT
#{'stu1102': 'Li', 1: 2, 3: 5, 'stu1101': 'Alex', 'stu1103': 'Zhang'}

#.iteam  字典转换成列表
print(a.items())


#.fromkeys  初始化字典

c = dict.fromkeys([1,2,3],{"name":"alex"})


print(c)


# 循环字典
#基本循环
for i in c:         #直接通过，字典索引 取值速度快
    print(i,c[1])
'''   :i 为key c[i] 为value
output
1 {'name': 'alex'}
2 {'name': 'alex'}
3 {'name': 'alex'}
'''
# 转换成列表 循环
for k,v in c.items():
    print(k,v)
# 输出结果一样，此种方法，会先将 字典转换成列表，然后通过下标，输出列表内容。效率低



#多级列表
data = {
    '北京': {
        '昌平': {
            '沙河':['蜀天晴','富雷'],
            '天通苑':['链家','yyyyy']
        },
        '朝阳':{
            '望京':["奔驰","陌陌"],
            '国贸':["CICC","HP"],
            '东直门':["Advent","飞信"]
        }
    },
    '山东': {
        '青岛': {
            '111': {
                1111:['222','33333'],
                1112:['222','33333'],
                1113:['222','33333']
            }
        },
        '济南': {
            '222': {
                11123:['2232','33434'],
                2323:['2324','2324']
            },
            '333': {
                3234:['232','3223'],
                3235:['232','3223']
            }
        }
    }
}
exit_falg = False
while not exit_falg:
    for i in data:
        print(i)
    choice = input("1>>:")
    if choice in data:
        while not exit_falg:
            for i2 in data[choice]:
                print('\t',i2)
            choice2 = input("2>>>:")
            if choice2 in data[choice]:
                while not exit_falg:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("3>>:")
                    if choice3 in data[choice][choice2]:
                        while not exit_falg:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t",i4)
                            choice4 = input(">>>: ")
                            if choice4 == "b":
                                break
                            elif choice4 == "q":
                                exit_falg = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_falg = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_falg = True
    if choice == "q":
        exit_falg = True