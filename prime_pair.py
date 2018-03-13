# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 13:08
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : prime_pair.py
# @Software: PyCharm Community Edition

'''

给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。
输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)）
输入描述:
输入包括一个整数n,(3 ≤ n < 1000)
输出描述:
输出对数
示例1
输入

10
输出

2
'''

# 1.查找N以内的素数

def find_prime_v1(N):
    L = list(range(2, N + 1))
    m = 0
    while m < L.__len__():
        n = m + 1
        while n < L.__len__():
            if L[n] % L[m] == 0:
                L.remove(L[n])
            n += 1
        m += 1
    return L


if __name__ == '__main__':
    n = int(raw_input())
    prime_list = find_prime_v1(n)
    counter = 0
    for i in range(prime_list.__len__()):
        if n - prime_list[i] in prime_list and n - prime_list[i] >= prime_list[i]:
            counter += 1
    print counter
