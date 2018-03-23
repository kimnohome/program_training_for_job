# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 13:50
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Fibonacci_array.py
# @Software: PyCharm Community Edition
'''
Fibonacci数列
题目描述
Fibonacci数列是这样定义的：
F[0] = 0
F[1] = 1
for each i ≥ 2: F[i] = F[i-1] + F[i-2]
因此，Fibonacci数列就形如：0, 1, 1, 2, 3, 5, 8, 13, ...，在Fibonacci数列中的数我们称为Fibonacci数。给你一个N，你想让其变为一个Fibonacci数，每一步你可以把当前数字X变为X-1或者X+1，现在给你一个数N求最少需要多少步可以变为Fibonacci数。
输入描述:
输入为一个正整数N(1 ≤ N ≤ 1,000,000)
输出描述:
输出一个最小的步数变为Fibonacci数"
示例1
输入

15
输出

2
'''

'''
斐波那契数列（Fibonacci sequence），
又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”
通项公式：
a_n=(1/sqrt(5))*( ((1+sqrt(5)/2)^n ) - ( (1-sqrt(5)/2)^n) )

从第二项开始，每个奇数项的平方都比前后两项之积多1，
每个偶数项的平方都比前后两项之积少1。
（注：奇数项和偶数项是指项数的奇偶，而并不是指数列的数字本身的奇偶，
比如从数列第二项1开始数，第4项5是奇数，但它是偶数项，如果认为5是奇数项，
那就误解题意，怎么都说不通）
除此之外还存在以下特点：
奇数项求和公式
偶数项求和公式
平方求和公式
隔项关系
两倍项关系
'''

if __name__ == '__main__':
    fibs = [0, 1]
    for i in range(40):
        fibs.append(fibs[-2] + fibs[-1])
    k=raw_input()
    k=int(k)
    k_=[k-i for i in fibs]
    k_=map(abs,k_)
    print min(k_)