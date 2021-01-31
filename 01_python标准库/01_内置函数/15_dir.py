# coding=utf-8
import struct


class Shape(object):
    def __dir__(self):
        return ['area', 'perimeter', 'location']


if __name__ == "__main__":
    print(dir())  # 打印当前本地作用域中的名称列表
    """
    ['Shape', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'struct']
    """
    print(dir(struct))  # 打印struct模块的名称列表
    """
    ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_clearcache', 'calcsize', 'error', 'iter_unpack', 'pack', 'pack_into', 'unpack', 'unpack_from']
    """

    ss = Shape()
    print(dir(ss))
    """
    ['area', 'location', 'perimeter']
    """

