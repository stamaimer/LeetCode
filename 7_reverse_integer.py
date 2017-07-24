# -*- coding: utf-8 -*-

"""
date: 07/24/17
author: stamaimer
source: https://leetcode.com/problems/reverse-integer/#/description
difficulty: easy
"""


class Solution(object):

    def reverse(self, x):

        digits = list()

        flag = 1 if x < 0 else 0

        x = -x if flag else x

        while x:

            x, digit = divmod(x, 10)

            digits.append(str(digit))

        reversed_integer = int(''.join(digits)) if digits else 0

        reversed_integer = -reversed_integer if flag else reversed_integer

        if reversed_integer < -pow(2, 31) or reversed_integer > pow(2, 31) - 1:

            return 0

        else:

            return reversed_integer

    def reverseV2(self, x):

        flag = -1 if x < 0 else 1

        x = int(str(abs(x))[::-1])

        if x >= pow(2, 31) - 1:

            return 0

        else:

            return x
