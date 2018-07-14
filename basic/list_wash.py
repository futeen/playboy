'''
1. 将列表中的年月日，相对应换成斜线。
2. 将￥符号去掉。

'''

a = ['2018年3月4日', '￥450', '134', '59']
b = 0
for x in a:
    for y in x:
        if y == '年':
            x = x.replace('年', '\\')
            a[b] = x
        elif y == '月':
            x = x.replace('月', '\\')
            a[b] = x
        elif y == '日':
            x = x.replace('日', '')
            a[b] = x
        elif y == '￥':
            x = x.replace('￥', '')
            a[b] = x
    b += 1

print(a[0])  # 2018\3\4
print(a) # ['2018\\3\\4', '450', '134', '59'], 第一个元素看似两条斜线，实际是一条
