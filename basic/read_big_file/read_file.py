# 500G, 特殊 一行
def myreadlines(f, newline):
    # 声明buf，类似缓存作用
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        # read方法在输入4096后，不会一次性读取全部文件，而是只读取4096个字符
        chunk = f.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf
            break
        buf += chunk


with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)

