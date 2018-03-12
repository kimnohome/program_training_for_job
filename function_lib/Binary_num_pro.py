# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 14:55
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Binary_num_pro.py
# @Software: PyCharm Community Edition
'''
这个脚本用于处理二进制数字
1.输出一个固定位数的二进制数，输入(1,3),输出001
'''


# 1.binary bit sighn
def bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


if __name__ == '__main__':
    # 1.
    print bin_digits(1, 3)
