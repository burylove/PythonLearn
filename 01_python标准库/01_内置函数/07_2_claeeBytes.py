# coding=utf-8

if __name__ == "__main__":
    strB = bytes("hello world", encoding="utf-8")
    intB = bytes(4)
    iterB = bytes([4, 5, 6, 128])
    iterB = bytes()

    print(strB)
    print(intB)
    print(iterB)
    print(iterB)

    with open("./7_1_bytearray.py", "r") as f:
        bufferB = bytes(f.read(), encoding="utf-8")
        print(bufferB)