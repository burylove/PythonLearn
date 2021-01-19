# coding=utf-8
class Test3(object): 
    def __init__(self):
        print("实例化test3")

class Test4():
    def __init__(self):
        print("实例化test4")

    def __complex__(self):
        return complex(3, 4)

if __name__ == "__main__":
    t1 = complex("2+3j")
    t2 = complex(4, 6)

    print(t1)   # (2+3j)
    print(t2)   # (4+6j)

    # t3 = complex(Test3())   # TypeError: complex() first argument must be a string or a number, not 'Test3'
    # print(t3)

    t4 = complex(Test4())   # 实例化test4
    print(t4)   # (3+4j)