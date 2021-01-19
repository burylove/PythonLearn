# coding=utf-8

def test1():
    print("调用test1")

class Test2():
    def __init__(self):
        print("实例化Test2")
test3 = "hello"

if __name__ == "__main__":
    if callable(test1): # 调用test1
        test1()
    else:
        print("不可调用")

    if callable(Test2): # 实例化Test2
        t2 = Test2()
    else:
        print("不可调用")

    if callable(test3): # 不可调用
        test3()
    else:
        print("不可调用")