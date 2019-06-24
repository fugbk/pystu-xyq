# Author：Li Ang
# encoding=utf8
name = input("Name:")
age = int(input("Age:"))
print(type(age))
job = input("Job:")
salary = input("Salary:")

info2 = '''
---------------info to {0}--------------
Name : {0}
Age  : {1}
Job  : {3}
Salary : {3}
'''.format(name,age,job,salary)

print(info2)
