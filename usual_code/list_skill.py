#输出一个列表a的元素，再输出一个列表b的元素
def list_adjust():
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8]
    c = []
    for x in range(len(a)):
        c.append(a[x])
        try:
            c.append(b[x])
        except IndexError:
            pass

    print(c)


if __name__ == "__main__":
    list_adjust()

