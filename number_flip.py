# -*- coding: utf-8 -*-
'''
@author: Kim Luo
@license: I don't kown,don't ask me
@contact: kim_luo_balabala@163.com
@software: @.@
@file: number_flip.py
@time: 18-3-20 下午3:13
@desc:
'''

'''
数字翻转,
题目描述
对于一个整数X，定义操作rev(X)为将X按数位翻转过来，并且去除掉前导0。例如:
如果 X = 123，则rev(X) = 321;
如果 X = 100，则rev(X) = 1.
现在给出整数x和y,要求rev(rev(x) + rev(y))为多少？
输入描述:

输入为一行，x、y(1 ≤ x、y ≤ 1000)，以空格隔开。

输出描述:

输出rev(rev(x) + rev(y))的值

示例1
输入

123 100

输出

223


'''

def rev(x):
    x_str=str(x)
    x_list=list(x_str)
    re_x_list=x_list[::-1]
    re_x_str=''.join(re_x_list)
    return int(re_x_str)


if __name__ == '__main__':
    # str_='123 100'
    str_ = raw_input()
    str_=str_.split(' ')
    x=int(str_[0])
    y=int(str_[1])
    print rev(rev(x)+rev(y))
