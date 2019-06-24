# Author：Li Ang
# encoding=utf8
name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")
info = '''
-------------- info of {_Name} -----------------
Name: {_Name}
Age : {_Age}
Job : {_Job}
Salary : {_Salary}
'''.format(_Name=name,
           _Age=age,
           _Job=job,
           _Salary=salary)
print(info)