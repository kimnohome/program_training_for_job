# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 13:41
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : geohash_incode.py
# @Software: PyCharm Community Edition
'''
题目描述
geohash编码：geohash常用于将二维的经纬度转换为字符串，分为两步：第一步是经纬度的二进制编码，
第二步是base32转码。此题考察纬度的二进制编码：算法对纬度[-90, 90]通过二分法进行无限逼近
（取决于所需精度，本题精度为6）。注意，本题进行二分法逼近过程中只采用向下取整来进行二分，
针对二分中间值属于右区间。算法举例如下： 针对纬度为80进行二进制编码过程：
1) 区间[-90, 90]进行二分为[-90, 0),[0, 90]，成为左右区间，可以确定80为右区间，标记为1；
2) 针对上一步的右区间[0, 90]进行二分为[0, 45),[45, 90]，可以确定80是右区间，标记为1；
3) 针对[45, 90]进行二分为[45, 67),[67,90],可以确定80为右区间，标记为1；
4) 针对[67,90]进行二分为[67, 78),[78,90]，可以确定80为右区间，标记为1；
5) 针对[78, 90]进行二分为[78, 84),[84, 90]，可以确定80为左区间，标记为0；
6) 针对[78, 84)进行二分为[78, 81), [81, 84)，可以确定80为左区间，标记为0；
输入描述:
输入包括一个整数n,(-90 ≤ n ≤ 90)
输出描述:
输出二进制编码
示例1
输入

80
输出

111100

唉，这个题主要坑的地方就是向下取整的地方（-63-68）/2得-66
而（63+68）/2得65，应该用所有数字的绝对值来处理取整之后再考虑正负号
'''

from math import floor, ceil


# binary bit sighn
def bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def judge_left_right(n, N_left, N_right):
    med = compute_med(N_left,N_right)
    if n < med and n >= N_left:
        return 0
    else:
        return 1


def compute_med(N_left, N_right):
    if N_right < 0:
        return -1 * int(floor((abs(N_left) + abs(N_right)) / 2))
    else:
        return int(floor((N_left + N_right) / 2))

if __name__ == '__main__':
    n = int(raw_input())
    #n = -66
    Num_incode_bits = 6
    a = bin_digits(0, Num_incode_bits)
    # print a
    # print int(a, 2)
    # print bin(int(a, 2) | 2 ** 5)
    N_left = -90
    N_right = 90
    for i in range(6):
        if judge_left_right(n, N_left, N_right):
            a = bin_digits(int(a, 2) | 2 ** (6 - i - 1), Num_incode_bits)
            N_left = compute_med(N_left, N_right)
        else:
            N_right = compute_med(N_left, N_right)
    print a
