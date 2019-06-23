# Author: LiAng
# encoding = utf-8
# Email : ali6102@163.com
import time
def deco(func): # <==> deco(test2) ------> func=test2
    def timer(*args,**kwargs): # ==> (*args,**kwargs) == ('ali')
        start_time = time.time()
        func(*args,**kwargs) # <==> test2('ali')
        stop_time = time.time()
        print("func run time is %s" %(stop_time - start_time))
    return timer
@deco  # <==> test2 = deco(test2(name))  name=str(ali)
def test2(name):
    time.sleep(1)
    print("in the test2 , I'm %s " %name)

test2('ali')