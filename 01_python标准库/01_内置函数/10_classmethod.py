# coding=utf-8

class Test(object):
    name = "李四"
    def __init__(self):
        self.name = "张三"
        print("实例化Test")
    
    def say(self):
        print(f"hello, {self.name}")
    
    @classmethod
    def hello(cls):
        print(f"你好, {cls.name}")

if __name__ == "__main__":
    Test.hello()    # 你好, 李四

    Test().say()
    """
    实例化Test
    hello, 张三
    """

    Test().hello()
    """
    实例化Test
    你好, 李四
    """

    Test.name = "王五"
    Test.hello() # 你好, 王五

    Test().hello()
    """
    实例化Test
    你好, 王五
    """
