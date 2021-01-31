# coding-utf-8
def func(x):
    return x % 2 == 0


if __name__ == "__main__":
    ll = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    tl = filter(func, ll)
    print(ll, list(tl))  # [0, 1, 2, 3, 4, 5, 6, 7, 8] [0, 2, 4, 6, 8]