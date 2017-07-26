# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/complex-number-multiplication/#/description
difficulty: easy
"""


class Solution(object):

    def complexNumnerMultiply(self, a, b):

        m, n = map(int, a[:-1].split('+'))
        o, p = map(int, b[:-1].split('+'))

        return str(m*o - n*p) + '+' + str(m*p + n*o) + 'i'
