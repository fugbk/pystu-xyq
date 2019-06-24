# Author：Li Ang
# encoding=utf8

'''
num = 4
count = 0
age = 30

while count < num:
    guess_age = int(input("your age: "))
    if guess_age < age:
        print("No, think smaller!")
    elif guess_age == age:
        print("Yes, you got it...")
        break
    else:
        print("No, think bigger!")
    count +=1

else:
    print("you have tried too many times,fuck off")
'''

'''
produce_list = [
    ('iphone',8000),
    ('book',4000),
    ('mac',18000),
    ('watch',3000)
]
sally = int(input("Your salary: "))
shopping_list = []
print("----------------Wellcome---------------")
while True:
    for index,item in enumerate(produce_list):
        print(index,item)
    choice = input("Your choice: ")
    print("-----------------------------------")
    if choice == "q":
        print("Goodby.")
        exit()
    choice = int(choice)
    choice_pice = int(produce_list[choice][1])
    if sally < choice_pice:
        print("It's not good idea, your sally not enough!")
    else:
        sally = sally - choice_pice
        shopping_list.append(produce_list[choice])
        print(shopping_list[0])
        print("Your shopping list is",shopping_list,"\n")
'''

produce_list = [
    ('iphone',8000),
    ('mac',18000),
    ('book',500),
    ('watch',4000)
]
sally = int(input("Your sally: "))
shopping_list = []
while True:
    print("--------------Wellcome---------------")
    for index,item in enumerate(produce_list):
        print(index,item)
    choice = input("Your choice: ")
    if choice == "q":
        print("Goodbye!")
    choice = int(choice)
    choice_pice = produce_list[choice][1]
    if sally < choice_pice:
        print("It's not good idea, your sally not enough!")
        exit()
    else:
        sally = sally - choice_pice
        shopping_list.append(produce_list[choice])
        print("Your sally is",sally,"your shopping list is:")
        for a,b in enumerate(shopping_list):
            print("\t",a,b)
        action = input("What to do next? ")       #n 继续购买，d 删除购物车商品
        if action == "n":
            continue
        elif action == "end":
            print("")
            exit()
        elif action == "d":
            del_goods = int(input("Goods number: "))
            shopping_list.pop(del_goods)
            for a,b in enumerate(shopping_list):
                print("\t",b)
                continue
#        print("\n")






















