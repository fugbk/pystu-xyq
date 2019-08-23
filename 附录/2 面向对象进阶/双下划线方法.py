class School:
    def __init__(self,name,addr,type):
        self.name = name
        self.addr = addr
        self.type = type
        print("对象创建....")

    def __del__(self):
        print("对象被释放了...")

s = School("yslm","beijing","magic")
print("dddddddddd")
