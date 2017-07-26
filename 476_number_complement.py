# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/number-complement/#/description
difficulty: easy
"""


class Solution(object):

    def findComplement(self, num):

        binary = "{0:b}".format(num)

        return int(''.join('1' if bit == '0' else '0' for bit in binary), 2)
