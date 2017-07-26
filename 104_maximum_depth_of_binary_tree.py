# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description
difficulty: easy
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def pre_order_traverse(self, node, temp, deep=0):

        deep += 1

        if node.left:

            self.pre_order_traverse(node.left, temp, deep)

        if node.right:

            self.pre_order_traverse(node.right, temp, deep)

        if not node.left and not node.right:

            temp.append(deep)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root:

            temp = list()

            self.pre_order_traverse(root, temp)

            return max(temp)

        else:

            return 0


if __name__ == '__main__':

    node_1 = TreeNode(1)

    node_2 = TreeNode(2)

    node_1.left = node_2

    Solution().minDepth(node_1)