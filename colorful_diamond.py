# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 17:19
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : colorful_diamond.py
# @Software: PyCharm Community Edition
'''
彩色宝石项链：
题目描述
有一条彩色宝石项链，是由很多种不同的宝石组成的，包括红宝石，蓝宝石，钻石，翡翠，珍珠等。有一天国王把项链赏赐给了一个学者，并跟他说，你可以带走这条项链，但是王后很喜欢红宝石，蓝宝石，紫水晶，翡翠和钻石这五种，我要你从项链中截取连续的一小段还给我，这一段中必须包含所有的这五种宝石，剩下的部分你可以带走。如果无法找到则一个也无法带走。请帮助学者找出如何切分项链才能够拿到最多的宝石。
输入描述:
我们用每种字符代表一种宝石，A表示红宝石，B表示蓝宝石，C代表紫水晶，D代表翡翠，E代表钻石，F代表玉石，G代表玻璃等等，我们用一个全部为大写字母的字符序列表示项链的宝石序列，注意项链是首尾相接的。每行代表一种情况。
输出描述:
输出学者能够拿到的最多的宝石数量。每行一个
示例1
输入

ABCYDYE
ATTMBQECPD
输出

1
3
'''

'''
我觉得应该是一个广度搜索的问题（扣除包含ABCDE的最短字符串）：
str_2=str+str
a=main_func_vX(str_2)#找到最短字符串长度
result=str.__len__()-a

'''

def judge_substr(str):
    if not'A' in str:
        return False
    if not'B' in str:
        return False
    if not'C' in str:
        return False
    if not'D' in str:
        return False
    if not'E' in str:
        return False
    return True

def find_shortest_num(a):
    #shortest_str =5
    for shortest_str in range(5,a.__len__()+1):
        for i in range(a.__len__()):
            if judge_substr(a[i:i + shortest_str]):
                return shortest_str

def main_func_v1(str):
    a=str+str
    shortest_num=find_shortest_num(a)
    return str.__len__()-shortest_num

if __name__ == '__main__':
    str=raw_input()
    print main_func_v1(str)