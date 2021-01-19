# coding=utf-8
class Num(object):
    def __init__(self, value):
        self.value = value
    def __abs__(self):
        return "绝对值"

if __name__ == "__main__":
    a = -1
    b = 3.14
    c = 0
    d = Num(666)
    print(f"{a}的绝对值是: {abs(a)}")   # -1的绝对值是: 1
    print(f"{b}的绝对值是: {abs(b)}")   # 3.14的绝对值是: 3.14
    print(f"{c}的绝对值是: {abs(c)}")   # 0的绝对值是: 0
    print(f"{d}的绝对值是: {abs(d)}")   # <__main__.Num object at 0x7feaaca58350>的绝对值是: 绝对值
