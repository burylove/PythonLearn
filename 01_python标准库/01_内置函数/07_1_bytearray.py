# coding=utf-8

if __name__ == "__main__":
    strB = bytearray("hello world", encoding="utf-8")
    intB = bytearray(4)
    iterB = bytearray([4, 5, 6, 128])
    iterB = bytearray()

    print(strB)
    print(intB)
    print(iterB)
    print(iterB)

    with open("./7_1_bytearray.py", "r") as f:
        bufferB = bytearray(f.read(), encoding="utf-8")
        print(bufferB)
