# Author：Li Ang
# encoding=utf8

product_list = [
    ('Mac Pro',9800),
    ('iphone',9900),
    ('book',77),
    ('watch',888),
    ('Bike',799),
]
shopping_list = []
salary = input("Your Salary >>> ")
if salary.isdigit():     # 如果是数字类型的 ，则True ， 有些数字以字符串形式存在，
    salary = int(salary)    # 如果是非数字， 强制转换int 可能会出 问题
    while True:
        print('--------------------Wellcome----------------------')
        # 同时取出下标和数据 ， 可以使用 enumerate函数， 效果相同
        #for line in product_list:
        #   print("\t",product_list.index(line),line)
        for index,item in enumerate(product_list):   #index,item 是enumerate 的方法
            print("\t",index,item)
        print('--------------------------------------------------')
        choice = input("Pleas input your choice >>> ")
        if choice.isdigit():
            choice = int(choice)
            #增加对 选项的判断， 大于0 ，小于 类别长度
            if choice >= 0 and choice <= len(product_list):
                p_item = product_list[choice]
                shopping_list.append(p_item)
                p_price = p_item[1]
                if salary >= p_price:
                    print(p_item,"add to your shopping list.")
                    salary = salary - p_price
                    print("Your sally is %s"%(salary))
                else:
                    print("Sorry not enough manny ！！！")
            else:
                print("Incorrect selection, please re - enter !!!")
        elif choice == 'q':
            print("Your shopping list",product_list)
            print("Your salary is",salary)
            exit(0)
        else:
            print("Incorrect selection, please re - enter !!!")
else:
    print("not int!!!")
