# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 9:27
# @Author  : Kim Luo
# @Email   : 287480609@qq.com
# @File    : Binary_tree.py
# @Software: PyCharm Community Edition
'''
目标是实现二叉树

作者：Jialin28
链接：https://www.jianshu.com/p/e86bc2c0d51c
來源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''

''' 树的构建： 
     5 
    6 7 
   8   9 
'''


class Tree_Node():
    # The realization of tree node
    def __init__(self, ltree=None, rtree=None, data=0):
        self.ltree = ltree
        self.rtree = rtree
        self.data = data


class BTree():
    # The realization of the binary tree
    def __init__(self, left_tree=None, right_tree=None, data=0):
        self.left_tree = left_tree
        self.right_tree = right_tree
        self.data = data

    def __end_tree(self):
        # check if the tree is empty
        if not self.left_tree and not self.right_tree:
            return True
        else:
            return False

    def add_left_chid(self, data):
        if not self.left_tree:
            self.left_tree = BTree(data=data)
            return
        else:  # left tree is not empty
            pass
        return

    def add_right_chid(self, data):
        if not self.right_tree:
            self.right_tree = BTree(data=data)
            return
        else:  # right tree is not empty
            pass
        return

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

    def in_order_out(self):
        # in-order traversal:left-root-right
        if self.__end_tree():
            print self.data
            return
        if self.left_tree:
            self.left_tree.in_order_out()
        print self.data
        if self.right_tree:
            self.right_tree.in_order_out()

    def post_order_out(self):
        # post-order traversal:left-right-root
        if self.__end_tree():
            print self.data
            return
        if self.left_tree:
            self.left_tree.post_order_out()
        if self.right_tree:
            self.right_tree.post_order_out()
        print self.data

    def layer_order_out(self):
        # implementation by queue
        qu_node = []
        node = self
        qu_node.append(node)
        while qu_node:
            node = qu_node.pop(0)
            print node.data
            if node.left_tree:
                qu_node.append(node.left_tree)
            if node.right_tree:
                qu_node.append(node.right_tree)

    def show(self):  # To implement a display tree
        pass


if __name__ == '__main__':
    tree1 = BTree(data=8)
    tree2 = BTree(data=9)
    tree3 = BTree(left_tree=tree1, data=6)
    tree4 = BTree(right_tree=tree2, data=7)
    base = BTree(left_tree=tree3, right_tree=tree4, data=5)
    print 'pre-order traversal:root-left-right:'
    base.pre_order_out()
    print 'in-order traversal:left-root-right:'
    base.in_order_out()
    print 'post-order traversal:left-right-root:'
    base.post_order_out()
    print 'layer order traversal:'
    base.layer_order_out()

'''
preorder traversal:root-left-right:
5
6
8
7
9
middle order traversal:left-root-right:
8
6
5
7
9
back order traversal:left-right-root:
8
6
9
7
5
'''
