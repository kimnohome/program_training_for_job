# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 13:07
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : game_task.py
# @Software: PyCharm Community Edition


'''游戏里面有很多各式各样的任务，其中有一种任务玩家只能做一次，
这类任务一共有1024个，任务ID范围[1,1024]。
请用32个unsigned int类型来记录着1024个任务是否已经完成。
初始状态都是未完成。 输入两个参数，都是任务ID，
需要设置第一个ID的任务为已经完成；并检查第二个ID的任务是否已经完成。
输出一个参数，如果第二个ID的任务已经完成输出1，如果未完成输出0。
如果第一或第二个ID不在[1,1024]范围，则输出-1,

输入包括一行,两个整数表示人物ID.
输出是否完成
示例1
输入

1024 1024
输出

1
'''

class task_incoder():
    def __init__(self):
        self.incode=range(10)


if __name__ == '__main__':
    task_ind = {}
    for i in range(1025):
        task_ind[str(i)] = 0
    a, b = raw_input().split(' ')
    a = int(a)
    b = int(b)
    if a < 1 or a > 1024 or b < 1 or b > 1024:
        print -1
    else:
        task_ind[str(a)] = 1
        print task_ind[str(b)]
