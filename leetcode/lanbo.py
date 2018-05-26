def auto_get():
    long = 'ababababacbab'
    short = 'aba'
    c = 0
    for x in range(len(long)-len(short)):
        if short == (long[:3]):
            c += 1
        long = long[1:]
    print(c)



if __name__ == "__main__":
    auto_get()
