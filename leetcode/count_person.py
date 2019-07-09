# 有17个人围成一圈（编号为：0 ~ 20），从第0号的人开始从8开始报数，
# 凡报到3的倍数的人离开圈子，然后再数下去。直到最后只剩下两个人为
# 止。问此人原来的位置是什么号码


def test(person, count=8):
    a = len(person)
    b = count
    for i in person:
        b += 1
        if len(person) == 2:
            return person
        if b % 3 == 0:
            b += 1
            person.remove(i)
    print(person)
    count += a
    return test(person, count)


person = list(range(20))
test(person)

