import codecs

with codecs.open('/Users/futeen/desktop/a.txt', encoding='utf16') as f:
    for rowx, row in enumerate(f):
        if row.endswith(u'\r\n'):
            row = row[:-2]
        data = row.split(u'\t')
        print(data)
        for colx, datum in enumerate(data):
            print(rowx, colx, repr(datum))
