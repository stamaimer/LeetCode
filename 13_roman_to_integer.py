# -*- coding: utf-8 -*-

"""
date: 07/24/17
author: stamaimer
source: https://leetcode.com/problems/roman-to-integer/#/description
difficulty: easy
"""


class Solution(object):

    def romanToInt(self, s):

        roman2int = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

        index = len(s) - 1

        sum = 0

        while index != -1:

            if index == 0:

                sum += roman2int[s[idnex]]

                break

            if roman2int[s[index]] > roman2int[s[index - 1]]:

                sum += roman2int[s[index]] - roman2int[s[index - 1]]

                index -= 2

            else:

                sum += roman2int[s[index]]

                index -= 1

        return sum

