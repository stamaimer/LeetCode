# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/merge-two-binary-trees/#/discuss
difficulty: easy
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pre_order_traverse(self, tree1, tree2, tree3):

        x = tree1.val if tree1 else 0
        y = tree2.val if tree2 else 0

        tree3.val = x + y

        tree1_left = tree1.left if tree1 and tree1.left else None
        tree2_left = tree2.left if tree2 and tree2.left else None

        if tree1_left or tree2_left:

            left = TreeNode(0)
            tree3.left = left
            self.pre_order_traverse(tree1_left, tree2_left, left)

        tree1_right = tree1.right if tree1 and tree1.right else None
        tree2_right = tree2.right if tree2 and tree2.right else None

        if tree1_right or tree2_right:

            right = TreeNode(0)
            tree3.right = right
            self.pre_order_traverse(tree1_right, tree2_right, right)

    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 or t2:

            t3 = TreeNode(0)

            self.pre_order_traverse(t1, t2, t3)

            return t3

        else:

            return None

    def mergeTreesV2(self, t1, t2):

        if (t1 is None) and (t2 is None):

            return None

        if t1 is None:

            return t2

        if t2 is None:

            return t1

        t1.val += t2.val

        t1.left = self.mergeTreesV2(t1.left, t2.left)
        t1.right = self.mergeTreesV2(t1.right, t2.right)

        return t1


if __name__ == '__main__':

    node_11 = TreeNode(1)

    node_12 = TreeNode(2)

    node_13 = TreeNode(3)

    node_15 = TreeNode(5)

    node_11.left = node_13

    node_11.right = node_12

    node_13.left = node_15

    node_21 = TreeNode(1)

    node_22 = TreeNode(2)

    node_23 = TreeNode(3)

    node_24 = TreeNode(4)

    node_27 = TreeNode(7)

    node_22.left = node_21

    node_22.right = node_23

    node_21.right = node_24

    node_23.right = node_27

    # Solution().mergeTrees(node_11, node_22)

    Solution().mergeTreesV2(node_11, node_22)
