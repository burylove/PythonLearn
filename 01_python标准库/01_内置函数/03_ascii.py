# coding=utf-8
class Stu(object):
    def __repr__(self):
        return "这是一个类的repr"

class Teacher(object):
    pass

if __name__ == "__main__":
    print(ascii(12345567))  #  12345567
    print(ascii("hello world!")) # 'hello world!'
    print(ascii("你好!"))    # '\u4f60\u597d!'

    s = Stu()
    t = Teacher()
    print(ascii(s)) # \u8fd9\u662f\u4e00\u4e2a\u7c7b\u7684repr
    print(ascii(t)) # <__main__.Teacher object at 0x7fd100259350
    


