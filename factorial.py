
from functools import reduce
def factorial(num):
    sum = 0
    l = []
    for x in range(1, num):
        for y in range(1, x+1):
            l.append(y)
        sum += reduce(lambda x,y:x*y, l)
        del l[:]
    print(sum)



def factorial2(num):
    a = range(1, num)
    sum = 0
    for i in a:
        tmp = 1
        for j in range(1, i + 1):
            tmp = tmp * j
        sum += tmp
    print(sum)

factorial(5)
factorial2(5)
