# encoding = utf-8
__author__ = "Ang Li"

class QQConnectionError(BaseException):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        num1 = int(num1)
        raise QQConnectionError("qq 连接错误") # 主动触发异常 (异常信息)
        num2 = int(num2)
        result = num1 + num2
    except QQConnectionError as e:
        print(e)
    except (EOFError,KeyboardInterrupt) as e:
        print(e)
    except NameError as e:
        print(e)
    except ValueError as e:
        print('出现异常，信息如下：')
        print(e)
    except Exception as e:
        print("万能异常")
 
