# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 22:06
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : top_title_recruit.py
# @Software: PyCharm Community Edition
'''
头条校招
题目描述
头条的2017校招开始了！为了这次校招，我们组织了一个规模宏大的出题团队，每个出题人都出了一些有趣的题目，而我们现在想把这些题目组合成若干场考试出来，在选题之前，我们对题目进行了盲审，并定出了每道题的难度系统。一场考试包含3道开放性题目，假设他们的难度从小到大分别为a,b,c，我们希望这3道题能满足下列条件：
a<=b<=c
b-a<=10
c-b<=10
所有出题人一共出了n道开放性题目。现在我们想把这n道题分布到若干场考试中（1场或多场，每道题都必须使用且只能用一次），然而由于上述条件的限制，可能有一些考试没法凑够3道题，因此出题人就需要多出一些适当难度的题目来让每场考试都达到要求，然而我们出题已经出得很累了，你能计算出我们最少还需要再出几道题吗？
输入描述:
输入的第一行包含一个整数n，表示目前已经出好的题目数量。

第二行给出每道题目的难度系数d1,d2,...,dn。

数据范围

对于30%的数据，1 ≤ n,di ≤ 5;

对于100%的数据，1 ≤ n ≤ 10^5,1 ≤ di ≤ 100。

在样例中，一种可行的方案是添加2个难度分别为20和50的题目，这样可以组合成两场考试：（20 20 23）和（35,40,50）。
输出描述:
输出只包括一行，即所求的答案。
示例1
输入

4
20 35 23 40
输出

2
'''


'''
看到最少，最多什么的，我就想到广度搜索，但是看到10^5，我想想还是有点虚
仔细看了一下，先排序，然后把相差10以上的块分开，每个块计算需要多少个题不就ok了

'''


def v1_main_func(NUM_pro, list_pro):
    a = sorted(list_pro)
    ind_1 = 0
    ind_2 = 0
    counter = 0
    for i in range(len(list_pro)-1):
        ind_2 += 1
        if a[ind_2] - a[ind_1] > 10:
            counter += v1_compute_block(a[ind_1:ind_2])
            ind_1 = ind_2
    if ind_1<ind_2:
        counter += v1_compute_block(a[ind_1:ind_2 + 1])  # include the final number
    elif ind_1 == ind_2:#a[-1]-a[-2]>10
        counter += 2
    else:
        pass  # wrong
    return counter



def v1_compute_block(list_block):
    len_list = len(list_block)
    if (len_list % 3) == 0:
        return 0
    else:
        return 3 - (len_list % 3)


if __name__ == '__main__':
    # NUM_pro = 4
    # list_pro = [1,2,3,3,5,20,21,30,39,48,60]
    NUM_pro = raw_input()
    list_pro_ = raw_input().split()
    list_pro = [int(s) for s in list_pro_]
    #print list_pro
    print v1_main_func(NUM_pro, list_pro)
