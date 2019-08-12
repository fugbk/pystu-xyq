# Author：Li Ang
# encoding=utf8
#购物车程序
product_list = [
    ('iphone',7000),
    ('mac',17000),
    ('book',10),
    ('watch',300)
]
# s = open('salary.txt','w+',encoding='utf-8')
# s.write('212121')
# salary = s.readline()
# shopping_list = []
# print(salary)
# f = open('shopping.txt','r+',encoding='utf-8')
# first_line = f.readline()
# print(first_line)
# f.close()
#
# l = open('product.txt','r',encoding='utf-8')
# r_product = open('product.txt','r',encoding='utf-8')
# product = r_product.read()

while True:
    print("---------Wellcome---------")
    for line in product_list:
        print(line)
    print("--------------------------")
    print('Your salary is: ',salary)
    choice = input("your choice:")
    if choice == "q":
        print("goodby")
        exit()
    choice = int(choice)
    if choice < len(product_list) and choice >= 0:
        choice_pice = int(product_list[choice][1])
        if salary >= choice_pice:
            salary = salary - choice_pice
            s.write(salary)
            shopping_list.append(product_list[choice])
            print("your salary is \033[0;31m%s\033[0m"%(salary))
            print("your shopping list is",shopping_list,"\n")
        else:
            print("It's not good idea,your salary not enough")
    else:
        print("Please input your choice 0 -",len(product_list)-1,"\n")
