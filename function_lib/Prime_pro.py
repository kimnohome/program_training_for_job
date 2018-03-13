# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 13:16
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Prime_pro.py
# @Software: PyCharm Community Edition
'''
拟用这个py来处理关于素数的问题：
1.查找N以内的素数
2.判断一个数是否是素数
'''
import math


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


# 2.判断一个数是否是素数
# 需要import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    print find_prime_v1(100)
    print isPrime(97)
