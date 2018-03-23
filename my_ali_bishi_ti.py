# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 18:25
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : my_ali_bishi_ti.py
# @Software: PyCharm Community Edition
'''
阿里的笔试题1，我的
'''
import Queue

if __name__ == '__main__':
    origin = raw_input()
    target = raw_input()

    q = Queue.Queue()
    q.put((origin, 0))
    visited = set()
    while not q.empty():
        current, depth = q.get()
        if current == target:
            break
        for i in range(len(current)):
            if int(current[i]) - 1 >= 1:
                new_num = current[:i] + str(int(current[i]) - 1) + current[i + 1:]
                if new_num not in visited:
                    visited.add(new_num)
                    q.put((new_num, depth + 1))
            if int(current[i]) + 1 <= 9:
                new_num = current[:i] + str(int(current[i]) + 1) + current[i + 1:]
                if new_num not in visited:
                    visited.add(new_num)
                    q.put((new_num, depth + 1))
        for i in range(len(current) - 1):
            for j in range(i + 1, len(current)):
                new_num = current[:i] + current[j] + current[i + 1:j] + current[i] + current[j + 1:]
                if new_num not in visited:
                    visited.add(new_num)
                    q.put((new_num, depth + 1))

    print depth