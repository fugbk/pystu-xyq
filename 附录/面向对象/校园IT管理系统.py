# encoding = utf-8
__author__ = "Ang Li"


class School(object):
    """总部学校"""
    def __init__(self, name, addr, website):
        self.name = name
        self.address = addr
        self.website = website
        self.balance = 0
        print("创建了校区【%s】，地址：【%s】，网址：【%s】" % (name, addr, website))

    def count_staff_num(self):
        """统计员工数量"""
        pass

    def count_stu_num(self):
        """统计学员数量"""
        pass

    def staff_enrollment(self, staff_obj):
        """员工入职"""
        pass

    def count_total_revenue(self):
        """统计总收入"""
        pass

    def count_class(self):
        """统计班级"""
        pass


class BranchSchool(School):
    """分校"""
    pass


class Course(object):
    """课程"""
    def __init__(self, name, price, outline):
        self.name = name
        self.price = price
        self.outline = outline
        print("创建了课程【%s】，学费【%s】" % (name, price))


class Class(object):
    def __init__(self, course_obj, semester, school_obj):
        self.coures_obj = course_obj
        self.semester = semester
        self.school_obj = school_obj
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
        return "%s-%s-%s" % (self.school_obj.name, self.coures_obj.name, self.semester)


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

    def push_card(self):
        pass


class Teacher(Staff):
    """教师"""
    def teacher_class(self, class_obj, day):
        print("教师【%s】在【%s】上课了【%s】天" % (self.name, class_obj, day))


class Student(object):
    def __init__(self,name,age,class_obj,balance):
        self.name = name
        self.age = age
        self.class_obj = class_obj # 学员报名的班级
        self.balance = balance # 学员的余额