# coding=utf-8
class Test(object):
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, addr: {self.addr}"


if __name__ == "__main__":
    tt = Test("zhangsan", 18, "北京")
    print(f"source: {tt}")  # source: name: zhangsan, age: 18, addr: 北京
    delattr(tt, "addr")  # delattr(tt, 'addr') 等价于 del tt.addr
    print(tt.name)  # 张三
    print(tt.age)   # 18
    print(tt.addr)  # AttributeError: 'Test' object has no attribute 'addr'
