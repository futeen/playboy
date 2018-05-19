def gen_fib(index):
    n,a,b = 0,0,1
    while n<index:
        yield b
        a,b = b, a+b
        n += 1

for data in gen_fib(10):
    print (data)
# print (gen_fib(10))
# 斐波拉契 0 1 1 2 3 5 8
# 这种方法不消耗内存
