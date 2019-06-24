# Author：Li Ang
# encoding=utf8

info = {
    'stu1101': "Level",
    'stu1102': "LiShi",
    'stu1103': "Wang",
}

print(info['stu1101'])

info['stu1101']="Test 01"

print(info['stu1101'])

del info['stu1101']

info.pop("stu1102")
print(info)



info.popitem()
print(info)

# print(info)

print(info.get('stu1101'))

print('stu1104' in info)

print(info.values())
print(info.keys())



info = {
    'stu1101': {
        'name':['ZangSi']
    },
    'stu1102': {
        'name':['LiSi']
    },
    'stu1103': {
        'name':['Wang']
    },
}

a = {
    'stu1101': {
        'name':['INFO']
    },
    'A': {
        'a':['1']
    },
    'B': {
        'b':['2']
    }
}

info.update(a)
print(info)

#info.setdefault('stu1105',{'name':['Test']})

print(info)


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
    choice = input("Your choice1 >>> ")
    if choice in data:
        while not exit_falg:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input("Your Choice2 >>> ")
            if choice2 in data[choice]:
                while not exit_falg:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input("Yuor choice3 >>> ")
                    if choice3 in data[choice][choice2]:
                        while not exit_falg:
                            for i4 in data[choice][choice2][choice3]:
                                print("\t\t\t",i4)
                            choice4 = input("Your choice4 >>> ")
                            if choice4 == "b":
                                break
                            else:
                                exit_falg = True
                    if choice3 == "b":
                        break
                    else:
                        exit_falg = True
            if choice2 == "b":
                break
            else:
                exit_falg = True
    if choice == "b":
        break
    else:
        exit_falg = True
