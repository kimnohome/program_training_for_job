# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 13:09
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : save_little_yi.py
# @Software: PyCharm Community Edition
'''
解救小易
题目描述
有一片1000*1000的草地，小易初始站在(1,1)(最左上角的位置)。小易在每一秒会横向或者纵向移动到相邻的草地上吃草(小易不会走出边界)。大反派超超想去捕捉可爱的小易，他手里有n个陷阱。第i个陷阱被安置在横坐标为xi ，纵坐标为yi 的位置上，小易一旦走入一个陷阱，将会被超超捕捉。你为了去解救小易，需要知道小易最少多少秒可能会走入一个陷阱，从而提前解救小易。
输入描述:
第一行为一个整数n(n ≤ 1000)，表示超超一共拥有n个陷阱。
第二行有n个整数xi，表示第i个陷阱的横坐标
第三行有n个整数yi，表示第i个陷阱的纵坐标
保证坐标都在草地范围内。
输出描述:
输出一个整数,表示小易最少可能多少秒就落入超超的陷阱
示例1
输入

3
4 6 8
1 2 1
输出

3
'''

'''
深度优先搜索
不对，直接x+y求最小
'''

if __name__ == '__main__':
    map_width=1000
    map_height=1000
    k=[[0 for j in range(map_height)] for i in range(map_width)]
    # print k
    # N_c=3
    # c_x=[4,6,8]
    # c_y=[1,2,1]
    N_c_s=raw_input()
    c_x_s=raw_input()
    c_y_s=raw_input()
    N_c=int(N_c_s)
    c_x=c_x_s.split()
    c_x=map(int,c_x)
    c_y=c_y_s.split()
    c_y=map(int,c_y)
    for i in range(N_c):
        k[c_x[i]][c_y[i]]=1
    list_map=[]
    list_step=[]
    list_map.append([0,0])
    list_step.append(0)

    list_step_s=[]
    for i in range(N_c):
        list_step_s.append(c_x[i]-1+c_y[i]-1)
    print min(list_step_s)
