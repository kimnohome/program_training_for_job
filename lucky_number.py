# -*- coding: utf-8 -*-
'''
幸运数:
题目描述
小明同学学习了不同的进制之后，拿起了一些数字做起了游戏。小明同学知道，在日常生活中我们最常用的是十进制数，而在计算机中，二进制数也很常用。现在对于一个数字x，小明同学定义出了两个函数f(x)和g(x)。 f(x)表示把x这个数用十进制写出后各个数位上的数字之和。如f(123)=1+2+3=6。 g(x)表示把x这个数用二进制写出后各个数位上的数字之和。如123的二进制表示为1111011，那么，g(123)=1+1+1+1+0+1+1=6。 小明同学发现对于一些正整数x满足f(x)=g(x)，他把这种数称为幸运数，现在他想知道，小于等于n的幸运数有多少个？
输入描述:

每组数据输入一个数n(n<=100000)

输出描述:

每组数据输出一行，小于等于n的幸运数个数。

示例1
输入

21

输出

3


'''

# 1.binary bit sighn
def bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def v1_main_test(n):
    cnt=0
    for i in range(1,n+1):
        # print i
        if g_x(i)==f_x(i):
            cnt+=1
    return cnt

def g_x(x):
    x=bin(x)
    y=x[2:]
    y_=list(y)
    return sum(map(int,y_))

def f_x(x):
    x=str(x)
    x_=list(x)
    return sum(map(int,x_))

if __name__ == '__main__':
    n=raw_input()

    n=int(n)
    print v1_main_test(n)