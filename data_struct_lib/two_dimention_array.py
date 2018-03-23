# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 12:48
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : two_dimention_array.py
# @Software: PyCharm Community Edition
'''
构建二维数组并且初始化
'''

if __name__ == '__main__':
    str='3,2'
    a,b=str.split(',')
    a=int(a)
    b=int(b)
    print a
    print b
    k=[[(j+1)*(i+1) for j in range(b)] for i in range(a)]
    print k
    print k[2][1]