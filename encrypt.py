import hashlib


def md_go():
    num = hashlib.md5()
    a = 'isearch123'
    num.update(a.encode(encoding='utf-8'))
    print(num.hexdigest())


if __name__ == "__main__":
    md_go()

