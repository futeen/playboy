def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return "done"


if __name__ == "__main__":
    # read_file("C:/Users/ThinkPad/Desktop/log.txt")
    a = fab(5)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())  # 报错StopIteration
