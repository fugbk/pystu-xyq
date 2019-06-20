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

