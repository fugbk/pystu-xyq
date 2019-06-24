# Author：Li Ang
# encoding=utf8


#用户输入参数， 打印参数
'''
username = input("username:")
password = input("password:")
print("username is " ,username ,"，password is" ,password  ,',,,,,,,,')
'''
#常量用引号引起来， 变量直接写变量名, 变量除外的都要用引号标识出来， 引号内username：是要输出的东西， 填写的参数会直接赋值给username
#input 标识从标准输入读取数据
'''
username is  Li ，password is redhat ,,,,,,,,
'''


#格式化输出
#一、字符串拼接
name = input("name:")
#age =  int(input("age:"))
age =  input("age:")
job = str(input("job:"))
salary = input("salary:")
"""
info = '''
-------------- info of ''' + name + ''' ------------
Name:''' + name + '''
Age: ''' + age + '''
Job: ''' + job + '''
'''

'''
-------------- info of Li ------------
Name:Li
Age: 23
Job: aaa
'''
"""
#在变量中引用变量 ，  对于变量部分使用 ''' + + ''' 标识  ；常量部分正常显示， 使用拼接的方式会开辟多个内存空间，影响程序运行效率。
#print(info)


#二、直接引用
"""
info = '''
---------- info of %s ----------
Name:%s
Age:%d
Job：%s
Salary:%s
''' % (name,name,age,job,salary)
"""

#.formart
info = '''
---------------info of to {user}------------------
Name:{user}
Age:{age}
Job:{job}
Salary:{salary}
'''.format(user=str(name),age=age,job=job,salary=salary)
print(info)

#输出结果
'''
---------- info of Li ----------
Name:Li
Age:23
Job：aaa
Salary:400000
'''

"""
%s  字符型
%d  整型
%f  浮点型
"""