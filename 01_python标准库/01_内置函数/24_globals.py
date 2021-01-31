# coding=utf-8
class Test(object):
    def __init__(self):
        self.name = "zhangsan"

    def run(self):
        print("runing")


if __name__ == "__main__":
    print(globals())
    """
    {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f9e5edb6fd0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '24_globals.py', '__cached__': None, 'Test': <class '__main__.Test'>}
    """