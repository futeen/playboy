# 从一个字符串中找出最长连续子字符串，输出其长度
# 想活的潇洒，活的自我，就得有顶得住一群傻逼瞎bb的心态，和说走就走的实力。有的人看着还行，但确实不值得跟他讲道理，浪费时间。
a = "abcdeacdabbcdffgeehabccdefh"
b = []
c = {}
d = []
e = []
f = []
g = []


def succession(a):
    count = 0
    for x in a:
        b.append(ord(x))
    for x in range(len(b)):
        if b[x] - b[x - 1] == 1:
            d.append(chr(b[x]))
        else:
            d.append("|")
    for x in range(1, len(d)):
        if d[x-1] == "|" and d[x] == "|":
            e.append(x-1)
    for x in range(len(e)):
        f.append(e[x] - count)
        count += 1
    for x in f:
        del d[x]
    for x in range(len(d)):
        if d[x] == "|":
            g.append(x)
    print(g)
    for x in range(1, len(g)):
        num = g[x] - g[x-1]
        print(num)




if __name__ == "__main__":
    succession(a)

