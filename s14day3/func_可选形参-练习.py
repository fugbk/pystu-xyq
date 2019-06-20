# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com


def build_person(first_name,last_name,age=''):
    persion = {'first_name':first_name,'last_name':last_name}
    if age:
        persion['age'] = age
    return persion

name_direct = build_person('Li','Ang',23)
print(name_direct)



# -*- coding: utf-8 -*-
def get_city_country(city,country):
    """输入 城市-国家 最多三次，输入q退出。"""
    home_town = city + ' ' + country
    return home_town.title()

count = 0
while True:
    count += 1
    if count > 3:
        exit()
    print('\n Please tell me your hometown')
    print('(inter \'q\' at any time to quit!)')

    city = input('Your city >>> ')
    if city == 'q':
        break
    country = input('Your country >>> ')
    if country == 'q':
        break
    format_hometown = get_city_country(city,country)
    print("\n Your hometown is ",format_hometown)

