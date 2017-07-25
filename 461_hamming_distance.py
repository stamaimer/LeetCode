# -*- coding: utf-8 -*-

"""
date: 07/25/17
author: stamaimer
source: https://leetcode.com/problems/hamming-distance/#/description
difficulty: easy
"""


class Solution(object):

    def hammingDistance(self, x, y):

        return sum(int(i) ^ int(j) for i, j in zip("{0:032b}".format(x), "{0:032b}".format(y)))
