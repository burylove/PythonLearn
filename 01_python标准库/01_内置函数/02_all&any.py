# coding=utf-8
if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,8,9,0]
    arr2 = ["", {}, 0]
    print(f"arr1的all: {all(arr1)}")    # arr1的all: False
    print(f"arr2的all: {all(arr2)}")    # arr2的all: False
    print(f"arr1的any: {any(arr1)}")    # arr1的any: True
    print(f"arr1的any: {any(arr2)}")    # arr1的any: False
