# encoding = utf-8
__author__ = "Ang Li"

import datetime


class School(object):
    """总部学校"""
    def __init__(self, name, addr, website):
        self.name = name
        self.address = addr
        self.website = website
        self.balance = 0
        self.branches = {}  # 下属分校
        self.class_list = []
        self.staff_list = {}
        self.branches[name] = self
        print("创建了校区【%s】, 地址:【%s】，网址:【%s】。" % (name, addr, website))

    def count_staff_num(self):
        """统计员工数量"""
        print("-----各校区员工数量-----")
        staff_total_num = 0
        for k,v in self.branches.items():
            branch_staff_num = len(v.staff_list)
            print("%s: %s" %(k,branch_staff_num))
            staff_total_num += branch_staff_num
        print("总计: %s" %(staff_total_num))

    def count_stu_num(self):
        """统计学员数量"""
        print("------学员数量--------")
        stu_total_num = 0
        for k,v in self.branches.items():
            branch_stu_num = 0
            for class_obj in v.class_list:
                branch_stu_num += len(class_obj.stu_list)
            print("%s: %s" %(k,branch_stu_num))
            stu_total_num += branch_stu_num
        print("总计: %s" %(stu_total_num))

    def staff_enrollment(self, staff_obj):
        """员工入职"""
        pass

    def count_total_revenue(self):
        """统计总收入"""
        print("--------校区总收入--------")
        total_balance = self.balance
        for k,v in self.branches.items():
            print("%s: %d" % (k,v.balance))
            total_balance += v.balance
        print("总收入:%s" % (total_balance))

    def count_class(self):
        """统计班级"""
        print("---------现有班级---------")
        for k,v in self.branches.items():
            for a in v.class_list:
                print(a)
    def count_branch_school(self):
        """统计校区"""
        print("-----------现有校区----------")
        for k,v in self.branches.items():
            print("%s地区: %s" %(v.address, v.name))


class BranchSchool(School):
    """分校"""
    def __init__(self, name, addr, website, headquater_obj):
        super().__init__(name,addr,website="www.lastack.com")
        self.headquater_obj = headquarter
        self.headquater_obj.branches[name] = self


class Course(object):
    """课程"""
    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.outline = outline
        print("创建了课程【%s】，学费【%s】。" % (name, price))


class Class(object):
    def __init__(self, course_obj, semester, school_obj):
        self.course_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
        self.stu_list = []
        school_obj.class_list.append(self)
        print("校区【%s】创建了班级【%s】，第【%s】学期。" % (school_obj.name, course_obj.name, semester))

    def stu_transfer(self, stu_obj, new_class_obj):
        """
        学员转校
        :param stu_obj: 学员对象
        :param new_class_obj:  转到的班级
        :return:
        """
        pass

    def __str__(self):
        return "%s-%s-%s" % (self.school_obj.name, self.course_obj.name, self.semester)


class Staff(object):
    """员工"""
    def __init__(self, name, age, balance, salary, position, dept, school_obj):
        self.name = name
        self.age = age
        self.balance = balance
        self.salary = salary
        self.position = position
        self.dept = dept
        self.school_obj = school_obj
        self.school_obj.staff_list[name] = self
        print("【%s】校区的【%s】部门，入职一位新员工【%s】，职位是【%s】。" %(school_obj.name,dept,name,position))
    def push_card(self):
        pass


class Teacher(Staff):
    """教师"""
    def __init__(self, name, age, balance, salary, position, dept, school_obj, course_obj):
        super().__init__(name, age, balance, salary, position, dept, school_obj)
        self.course_obj = course_obj
     #   print("教师【%s】在【%s】校区入职,教授【%s】, 月薪【%s】。" %(name,school_obj.name,course_obj.name,salary))

    def teacher_class(self, class_obj, day):
        print("教师【%s】在【%s】上课了【%s】天" % (self.name, class_obj, day))


class Student(object):
    def __init__(self,name,age,class_obj,balance):
        self.name = name
        self.age = age
        self.class_obj = class_obj # 学员报名的班级
        self.balance = balance # 学员的余额
        # 加入班级
        class_obj.stu_list.append(self)
        # 扣除学费
        self.balance -= class_obj.course_obj.price
        # 增加校区收入
        class_obj.school_obj.balance += class_obj.course_obj.price
        print("%s 招收了学员【%s】在【%s】班，交了学费【%s】，生活费剩余【%s】。" %(datetime.datetime.now(),name,class_obj,class_obj.course_obj.price,self.balance))

    def punch_card(self):
        """学员打开"""
        print("%s-学员[%s] 在班级[%s] 上课了......" %(datetime.datetime.now(),self.name,self.class_obj))


# 实例化校区
headquarter = School("北京总部", "北京昌平", "www.lastack.com")
sz1 = BranchSchool("失落国度","深圳南山","www.lastack.com", headquarter)
sz2 = BranchSchool("虹桥计划","深圳安良","www.lastack.com", headquarter)
sh1 = BranchSchool("安良拓荒","上海虹桥","www.lastack.com", headquarter)
sh2 = BranchSchool("要素黎明","上海边江","www.lastack.com", headquarter)

# 实例化课程
knight = Course("骑士训练",20333,"all")
magic = Course("魔法师养成",32222,"all")
pharmaceutics = Course("药剂师养成",76666,"all")
hunter = Course("猎人训练",9898,"all")
assassin = Course("刺客信条",43998,"all")

# 实例化班级
knight_class = Class(knight,18,sz1)
magic_class = Class(magic,23,sz2)
pharmaceutics_class = Class(pharmaceutics,3,sh1)
hunter_class = Class(hunter,36,sh2)
assassin_class = Class(assassin, 7, headquarter)

# 实例化员工
staff1 = Staff("朱莉", 17, 0, 6000,"接待","运营部", headquarter)
staff2 = Staff("特莉诗",18,0,6500,"图书管理员","后勤部",sz2)
staff3 = Staff("依莲",18,0,7000,"HR","总经办",sh2)
staff4 = Staff("霍尔",18,0,8000,"保安","保卫部",sh1)
staff5 = Staff("埃姆林",18,0,7500,"司机","后勤部",sz1)

# 实例化教师
teacher1 =  Teacher("阿兹克", 31, 0, 22000,"骑士教师","教学部", headquarter, knight)
teacher2 = Teacher("戴莉",26,0,20000,"魔法教师","教学部",sh2,magic)
teacher3 = Teacher("辛克蕾尔",25,0,27000,"猎人教师","教学部",sh2,hunter)
teacher4 = Teacher("依兰尼",23,0,22000,"药剂教师","教学部",sz2,pharmaceutics)

# 实例化学员
stu1 = Student("李察.阿克蒙德",13,knight_class,1000000)
stu2 = Student("克莱恩.莫雷蒂",19,magic_class,30000)
stu3 = Student("芙蕾雅",15,pharmaceutics_class,200000)
stu4 = Student("伦纳德",17,hunter_class,40000)
stu5 = Student("艾德莉亚",15,magic_class,80000)
stu6 = Student("奥黛丽",18,assassin_class,7000000)


# 统计现有校区
headquarter.count_branch_school()

# 统计现有班级
headquarter.count_class()

# 统计校区总收入
headquarter.count_total_revenue()

# 统计校区员工数
headquarter.count_staff_num()

# 统计校区学员数
headquarter.count_stu_num()