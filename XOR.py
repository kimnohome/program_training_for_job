# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:16
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : XOR.py
# @Software: PyCharm Community Edition
'''
目标诺森德,异或
题目描述
给定整数m以及n各数字A1,A2,..An，将数列A中所有元素两两异或，共能得到n(n-1)/2个结果，请求出这些结果中大于m的有多少个。
输入描述:
第一行包含两个整数n,m.

第二行给出n个整数A1，A2，...，An。

数据范围

对于30%的数据，1 <= n, m <= 1000

对于100%的数据，1 <= n, m, Ai <= 10^5
输出描述:
输出仅包括一行，即所求的答案
示例1
输入

3 10
6 5 10
输出

2
'''
'''
v1:先暴力搜索一遍看看

v2:查了一下关于异或算法：
a^b>=a-b
a^b=c => a^c=b
把这个不等式加到暴力搜索里面可以减少一些运算
就是说对于Ai，只对比[Ai-m,Ai)范围内的数就可以了

v3:看了一下评论，最关键的关键点在于：从高位到地低位，如果m在某位为0，
而对于A在这一位上如果有B能使得A^B在这一位为1则A^B一定比m大（从高位到低位搜索）
所以需要建立一个二叉树来搞这个问题
'''


# 1.binary bit sighn
def v3_bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


class v3_tree():
    pass

def v3_main_func(n, m, list_pro):
    temp = max(list_pro)
    temp = max(temp, m)
    N_bit = len(bin(temp))  # number of needed bits
    for i in range(len(list_pro)):
        pass


def v2_compute_func(Ai, list_after_Ai, m):  # list_afterAi need to be big-->small
    cnt = 0
    rank = Ai - m
    for i in range(len(list_after_Ai)):
        if list_after_Ai[i] < rank:
            return cnt + len(list_after_Ai[i:])
        if Ai ^ list_after_Ai[i] > m:
            cnt += 1
    return cnt


def v2_main_func(n, m, list_pro):
    cnt = 0
    a = sorted(list_pro)
    a = a[::-1]
    for i in range(len(a) - 1):
        cnt += v2_compute_func(a[i], a[i + 1:], m)
    return cnt


def v1_main_func(n, m, list_pro):
    cnt = 0
    for i in range(len(list_pro) - 1):
        for j in range(i + 1, len(list_pro)):
            if list_pro[i] ^ list_pro[j] > m:
                cnt += 1
    return cnt

if __name__ == '__main__':
    n, m = raw_input().split()
    n = int(n)
    m = int(m)
    list_pro_ = raw_input().split()
    list_pro = [int(s) for s in list_pro_]

    # n = 3
    # m = 10
    # list_pro = [6, 5, 10]

    print v2_main_func(n, m, list_pro)
