# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 10:24
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : grid_walk.py
# @Software: PyCharm Community Edition
'''
网格走法数目
题目描述
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。
输入描述:
输入包括一行，逗号隔开的两个正整数x和y，取值范围[1,10]。
输出描述:
输出包括一行，为走法的数目。
示例1
输入

3 2
输出

10
'''


def get_map_point(temp_i, temp_j, k_map):
    row = len(k_map)
    column = len(k_map[temp_i])
    cnt = 0
    if temp_i==row-1 and temp_j==column-1:
        return 1
    if temp_i + 1 < row:
        cnt = cnt + k_map[temp_i + 1][temp_j]
    if temp_j + 1 < column:
        cnt = cnt + k_map[temp_i][temp_j + 1]
    return cnt


if __name__ == '__main__':
    # str = '3,2'
    str=raw_input()
    a, b = str.split()
    a = int(a)+1
    b = int(b)+1
    # print a
    # print b
    k_map = [[0 for j in range(b)] for i in range(a)]
    # print k_map
    # print k_map[2][1]
    # print len(k_map)
    ind_row = a - 1
    ind_column = b - 1
    k_map[ind_row][ind_column] = 1
    for i in range(a):
        for j in range(b):
            temp_i = ind_row - i
            temp_j = ind_column - j
            k_map[temp_i][temp_j] = get_map_point(temp_i, temp_j, k_map)
    print k_map[0][0]
