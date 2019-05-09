# the way using of lambda and map


def f(x):
    return x * x


def test_map():
    a = map(f, [1, 2, 3, 4, 5, 6])
    for x in a:
        print(x)


def test_map_lambda():
    b = map(lambda x, y: x ** y, [1, 2, 3], [2, 3, 4])
    for x in b:
        print(x)
    print('-----------')

    c = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 3])
    for y in c:
        print(y)

    print('------------')
    # type convert
    d = map(int, '1234')
    for z in d:
        print(z, type(z))


if __name__ == "__main__":
    test_map()
    print('---------')
    test_map_lambda()

