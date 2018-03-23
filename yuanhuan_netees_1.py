# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 18:48
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : yuanhuan_netees_1.py
# @Software: PyCharm Community Edition
'''
袁欢，网易实习招聘笔试，1

'''

if __name__ == '__main__':
    k=raw_input().split()
    a=map(int,k)
    m=a[0]
    n=a[1]
    if m==1:
        print n
    else:
        a_n=(m-1)**n+(-1)**(n-2)*(m-1)
        print a_n