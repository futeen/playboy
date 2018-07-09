'''
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]

'''

import numpy as np


def transpose_matrix():
    mtr = np.arange(24).reshape(4, 6)
    print(mtr)
    matrix = []
    matrix_list = []
    num = 0
    for y in range(len(mtr[0])):
        for x in range(len(mtr)):
            matrix_list.append(mtr[x][num])
        num += 1
    print('+++++++++++++++')
    c = int((len(mtr[0])/len(mtr)))
    print(c)
    for x in range(len(mtr[0])):
        matrix.append(matrix_list[:len(mtr)])
        del matrix_list[:len(mtr)]
    print(matrix)


if __name__ == "__main__":
    transpose_matrix()

