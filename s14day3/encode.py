# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com


s = "我"     # 默认unicode 编码
print(s)

s_to_gbk = s.encode('gbk')
print(s_to_gbk,'gbk')

s_to_utf8 = s.encode('utf-8')
print(s_to_utf8,'utf-8')

s_to_unicode = s_to_utf8.decode('utf-8')
print(s_to_unicode,'unicode')

def test(x):
    "The funcation test"
    x += 1
    return x

# def 函数定义方法
# test 函数名称
# （） 内可定义形参
# x += 1 代码逻辑块
# return 返回值
# " "     函数描述语句