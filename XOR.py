# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 11:16
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : XOR.py
# @Software: PyCharm Community Edition
'''
目标诺森德,异或
题目描述
给定整数m以及n各数字A1,A2,..An，将数列A中所有元素两两异或，共能得到n(n-1)/2个结果，请求出这些结果中大于m的有多少个。
输入描述:
第一行包含两个整数n,m.

第二行给出n个整数A1，A2，...，An。

数据范围

对于30%的数据，1 <= n, m <= 1000

对于100%的数据，1 <= n, m, Ai <= 10^5
输出描述:
输出仅包括一行，即所求的答案
示例1
输入

3 10
6 5 10
输出

2
'''
'''
v1:先暴力搜索一遍看看

v2:查了一下关于异或算法：
a^b>=a-b
a^b=c => a^c=b
把这个不等式加到暴力搜索里面可以减少一些运算
就是说对于Ai，只对比[Ai-m,Ai)范围内的数就可以了

v3:看了一下评论，最关键的关键点在于：从高位到地低位，如果m在某位为0，
而对于A在这一位上如果有B能使得A^B在这一位为1则A^B一定比m大（从高位到低位搜索）
所以需要建立一个二叉树来搞这个问题
左节点为1,右节点为0
例如：
m_i=0  a_i=0所以cnt加上左节点的数量，然后node=右节点继续迭代
m_i=0  a_i=1所以cnt加上右节点的数量，然后node=左节点继续迭代
m_i=1  a_i=0所以cnt不变，然后node=左节点继续迭代
'''


class v3_BTree():
    # The realization of the binary tree
    def __init__(self, left_tree=None, right_tree=None, data=0,depth=0):
        self.left_tree = left_tree
        self.right_tree = right_tree
        self.data = data
        self.depth= depth

    def __end_tree(self):
        # check if the tree is empty
        if not self.left_tree and not self.right_tree:
            return True
        else:
            return False

    def pre_order_out(self):
        # pre-order traversal:root-left-right
        if self.__end_tree():
            print self.data
            return
        print self.data
        if self.left_tree:
            self.left_tree.pre_order_out()
        if self.right_tree:
            self.right_tree.pre_order_out()

    def update_with_char_list(self, char_list):
        self.data += 1
        if not char_list:
            return

        a = char_list.pop(0)
        if a == '1':
            if not self.left_tree:
                self.left_tree = v3_BTree()
                self.left_tree.depth=self.depth+1
            self.left_tree.update_with_char_list(char_list)
        elif a == '0':
            if not self.right_tree:
                self.right_tree = v3_BTree()
                self.right_tree.depth=self.depth+1
            self.right_tree.update_with_char_list(char_list)

    def update_right_chid(self, char_list):
        pass

    def layer_order_out(self):
        # implementation by queue
        qu_node = []
        node = self
        qu_node.append(node)
        while qu_node:
            node = qu_node.pop(0)
            print '(%d)%d'%(node.depth, node.data)
            if node.left_tree:
                qu_node.append(node.left_tree)
            if node.right_tree:
                qu_node.append(node.right_tree)

                    # 1.binary bit sighnn


def v3_bin_digits(n, bits):
    s = bin(n & int("1" * bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)


def v3_read_tree_xor(base, list_M, list_sample):
    cnt = 0
    node = base
    for i in range(len(list_M)):
        if list_M[i] == '1':  # m_ibit=1
            if list_sample[i] == '1':  # a_ibit=1
                if node.right_tree:
                    node=node.right_tree # b_ibit need to be 0
                else:
                    return cnt
            else:  # a_ibit=0
                if node.left_tree:
                    node = node.left_tree  # b_ibit need to be 1
                else:
                    return cnt
        else:# m_ibit=0
            if list_sample[i] == '1':# a_ibit=1
                if node.right_tree:
                    cnt+=node.right_tree.data
                if node.left_tree:
                    node=node.left_tree
                else:
                    return cnt
            else:# a_ibit=0
                if node.left_tree:
                    cnt+=node.left_tree.data
                if node.right_tree:
                    node=node.right_tree
                else:
                    return cnt
    return cnt

def v3_main_func(n, m, list_pro):
    #test
    # a=v3_bin_digits(m,3)
    # print 'a=%s'%a
    # a=list(a)
    # print a
    # base=v3_BTree()
    # base.update_with_char_list(a)
    # base.layer_order_out()

    temp = max(list_pro)
    temp = max(temp, m)
    N_bit = len(bin(temp))-2  # number of needed bits:bin(10)->'0b1010'
    M_binary=list(v3_bin_digits(m,N_bit))
    base = v3_BTree()
    counter=0
    for i in range(len(list_pro)):
        # a=v3_bin_digits(list_pro[i],N_bit)
        # print a
        base.update_with_char_list(list(v3_bin_digits(list_pro[i],N_bit)))
    for ii in range(len(list_pro)):
        counter+=v3_read_tree_xor(base,M_binary,list(v3_bin_digits(list_pro[ii],N_bit)))
    return counter/2


def v2_compute_func(Ai, list_after_Ai, m):  # list_afterAi need to be big-->small
    cnt = 0
    rank = Ai - m
    for i in range(len(list_after_Ai)):
        if list_after_Ai[i] < rank:
            return cnt + len(list_after_Ai[i:])
        if Ai ^ list_after_Ai[i] > m:
            cnt += 1
    return cnt


def v2_main_func(n, m, list_pro):
    cnt = 0
    a = sorted(list_pro)
    a = a[::-1]
    for i in range(len(a) - 1):
        cnt += v2_compute_func(a[i], a[i + 1:], m)
    return cnt


def v1_main_func(n, m, list_pro):
    cnt = 0
    for i in range(len(list_pro) - 1):
        for j in range(i + 1, len(list_pro)):
            if list_pro[i] ^ list_pro[j] > m:
                cnt += 1
    return cnt


if __name__ == '__main__':
    n, m = raw_input().split()
    n = int(n)
    m = int(m)
    list_pro_ = raw_input().split()
    list_pro = [int(s) for s in list_pro_]

    # n = 942
    # m = 6
    # # k=''
    # kk=k.split()
    # list_pro = map(int,kk)
    # list_pro = [6, 5, 10,92,4898,35,4865,568,68]
    # list_pro=range(7)
    # print v1_main_func(n,m,list_pro)
    print v3_main_func(n, m, list_pro)
