# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 15:47
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : strong_brain.py
# @Software: PyCharm Community Edition
'''
题目：最强大脑
题目描述
小B乘火车和朋友们一起在N市到M市之间旅行。她在路途中时睡时醒。
当她醒来观看窗外的风景时，注意到每个火车站都有一种特别颜色的旗帜，
但是她看到的旗帜仅仅是经过的一小部分。小B在乘车过程中有两次清醒的时间，
她到达旅程终点时处于睡梦中。出站时，她和朋友们谈论着一路的见闻，朋友们觉得很有意思，
他们把N到和M之间经过车站的旗帜颜色依次列出来，然后告诉你小B记得的旗帜颜色序列，
让你判断小B究竟是从N和M之间哪些方向才能看到所说颜色的旗帜，还是根本就不可能看到？
颜色用字母代表，相同的字母代表相同的颜色，不同的字母则表示不同的颜色。
输入描述:
输入中有多组测试数据，每组测试数据包含三行，第一行为一个由小写拉丁字母构成的非空字符串，
长度不超过10^5，表示N到M之间车站的颜色。火车从M向N运行时，经过的车站相同，只是方向相反。
第二行为小B在第一次睡醒时看到的颜色序列，第三行为小B在第二次睡醒时看到的颜色序列。
两个序列都是小写的拉丁字母构成的字符串，长度不超过100个字母。
每个序列的颜色顺序排列按小B看到的时间顺序排列。
输出描述:
对每组测试数据，在单独的行中输出小B的旅行方向。

forward - 由N到M方向；

backward -由M到N方向

both - 两种方向都有可能；

invalid - 不可能看到这样的颜色序列；
示例1
输入

atob
a
b
aaacaaa
aca
aa
输出

forward
both
'''

'''
str.find找不到会返回-1，str.index找不到会报错
我出的问题关键再正序反序中，我是搜索序列位置前后，而没有考虑序列顺序前后变化
main_func_v1只能判断正向的情况
'''


def main_func_v1(N_M, str_1, str_2):
    if (N_M.find(str_1) == -1 or N_M.find(str_2) == -1) and (
                    N_M[::-1].find(str_1) == -1 or N_M[::-1].find(str_1) == -1):
        return 'invalid '
    a_ind_1 = N_M.index(str_1)
    a_ind_2 = N_M.rindex(str_1)
    b_ind_1 = N_M.index(str_2)
    b_ind_2 = N_M.rindex(str_2)
    if a_ind_1 == a_ind_2 and b_ind_1 == b_ind_2:
        if a_ind_1 < b_ind_1:
            return 'forward '
        else:
            return 'backward '
    elif a_ind_1 < b_ind_1 and a_ind_1 < b_ind_2 and a_ind_2 < b_ind_1 and a_ind_2 < b_ind_2:
        return 'forward'
    elif a_ind_1 > b_ind_1 and a_ind_1 > b_ind_2 and a_ind_2 > b_ind_1 and a_ind_2 > b_ind_2:
        return 'backward'
    else:
        return 'both'


def return_direction(a, b):  # b==1:forword; a==1:single direction
    if a == 1:
        if b == 1:
            return 'forward'
        else:
            return 'backward'
    else:
        return 'both'


def judge_direction(N_M, str_1, str_2):
    a_ind_1 = N_M.index(str_1)
    a_ind_2 = N_M.rindex(str_1)
    b_ind_1 = N_M.index(str_2)
    b_ind_2 = N_M.rindex(str_2)
    if a_ind_1 == a_ind_2 and b_ind_1 == b_ind_2:
        if a_ind_1 > b_ind_1:
            return 0
        else:
            return 1
    elif a_ind_1 <= b_ind_1 or a_ind_1 <= b_ind_2 or a_ind_2 <= b_ind_1 or a_ind_2 <= b_ind_2:
        return 1
    else:
        return 0


def main_func_v2(N_M, str_1, str_2):
    if (N_M.find(str_1) == -1 or N_M.find(str_2) == -1) and (
                    N_M[::-1].find(str_1) == -1 or N_M[::-1].find(str_1) == -1):
        return 'invalid'
    if N_M.find(str_1) != -1 or N_M.find(str_2) != -1:  # zheng
        a = judge_direction(N_M, str_1, str_2)
    else:
        a = -1
    if N_M[::-1].find(str_1) != -1 or N_M[::-1].find(str_1) != -1:
        b = judge_direction(N_M[::-1], str_1, str_2)  # fan
    else:
        b = -1
    if a == 1 and b == 1:
        return return_direction(2, 1)
    elif a == 1 and b != 1:
        return return_direction(1, 1)
    elif a != 1 and b == 1:
        return return_direction(1, 0)
    else:
        print a, b
        return 'invalid'


def main_func_v3(N_M, str_1, str_2):
    ok_flag_forward = True
    ok_flag_backward = True
    if N_M.find(str_1) == -1 or N_M.find(str_2) == -1:  # forward false
        ok_flag_forward = False
    else:
        if can_tong(N_M, str_1, str_2):
            ok_flag_forward = True
        else:
            ok_flag_forward = False
    if N_M[::-1].find(str_1) == -1 or N_M[::-1].find(str_1) == -1:  # backward false
        ok_flag_backward = False
    else:
        if can_tong(N_M[::-1], str_1, str_2):
            ok_flag_backward = True
        else:
            ok_flag_backward = False
    if ok_flag_forward and ok_flag_backward:
        return 'both'
    elif ok_flag_forward:
        return 'forward'
    elif ok_flag_backward:
        return 'backward'
    else:
        return 'invalid'


def can_tong(N_M, str_1, str_2):
    a = N_M.index(str_1)
    b = N_M[(a + str_1.__len__()):].find(str_2)
    if b == -1:
        return False
    else:
        return True

if __name__ == '__main__':
    # print main_func()
    # print main_func('atob','a','b')
    N_M = raw_input()
    str_1 = raw_input()
    str_2 = raw_input()
    # N_M = 'atob'
    # str_1 = 'a'
    # str_2 = 'b'
    print main_func_v3(N_M, str_1, str_2)
