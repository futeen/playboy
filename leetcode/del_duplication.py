# 列表内容去重，不用集合方式，按照原列表顺序不变
a = [1, 1, 2, 3, 2, 1, 6, 7, 5, 4, 3, 8, 4, 4, 3, 2, 6, 6]


def wipe_dup(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    print(b)


if __name__ == "__main__":
    wipe_dup(a)
