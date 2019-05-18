import pandas as pd
import numpy as np


def pandas_sort():
    df = pd.DataFrame({'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
                       'col2': [2, 1, 9, 8, 7, 7],
                       'col3': [0, 1, 9, 4, 2, 8]
                       })

    # 依据第一列排序，并将该列空值放在首位
    one = df.sort_values(by=['col1'], na_position='first')
    '''
      col1  col2  col3
    3  NaN     8     4
    0    A     2     0
    1    A     1     1
    2    B     9     9
    5    C     7     8
    4    D     7     2

    '''

    # 依据第二、三列，数值降序排序
    two = df.sort_values(by=['col2', 'col3'], ascending=False)
    '''
      col1  col2  col3
    2    B     9     9
    3  NaN     8     4
    5    C     7     8
    4    D     7     2
    0    A     2     0
    1    A     1     1

    '''

    # 根据第一列中数值排序，按降序排列，并替换原数据
    three = df.sort_values(by=['col1'], ascending=True, inplace=False, na_position='first')
    '''
      col1  col2  col3
    3  NaN     8     4
    0    A     2     0
    1    A     1     1
    2    B     9     9
    5    C     7     8
    4    D     7     2
    '''

    x = pd.DataFrame({'x1': [1, 2, 2, 3], 'x2': [4, 3, 2, 1], 'x3': [3, 2, 4, 1]})

    # 按照索引值为0的行，即第一行的值来降序排序, axis=0 列， axis=1, 行
    four = x.sort_values(by=0, ascending=False, axis=1)
    '''
       x2  x3  x1
    0   4   3   1
    1   3   2   2
    2   2   4   2
    3   1   1   3
    '''
    print(x.mean(axis=1))


if __name__ == "__main__":
    pandas_sort()

