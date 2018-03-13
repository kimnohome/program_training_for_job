# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 15:45
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : temp_test.py
# @Software: PyCharm Community Edition
'''
用来做测试随便用
'''

# 1.binary bit sighn
def bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

if __name__ == '__main__':
    a=[1,2,3,4]
    tree=[]
    for i in range(len(a)):
        #temp=[int(s) for s in list(bin_digits(a[i],3))]
        temp=map(int,list(bin_digits(a[i],3)))
        tree.append(temp)
    print tree
    print sum(tree[::][1])
    print [x[0] for x in tree]
