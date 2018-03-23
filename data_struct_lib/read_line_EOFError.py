# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 13:48
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : read_line_EOFError.py
# @Software: PyCharm Community Edition
'''
有时候要一直读input，判断EOF的办法就是try-except
'''


def group_ID(a):
    if len(a)<=6:
        return a
    elif len(a)<=6+8:
        return a[0:6] + ' ' + a[6::]
    elif len(a)<=6+8+4:
        return a[0:6] + ' ' + a[6:6+8] + ' ' + a[6+8::]

if __name__ == '__main__':
    flag=1
    try:
        while flag == 1:
            str = raw_input()
            if len(str) == 18:
                flag = 0
            print group_ID(str)
    except EOFError:
        flag=0