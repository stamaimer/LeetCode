# -*- coding: utf-8 -*-

"""
date: 07/24/17
author: stamaimer
source: https://leetcode.com/problems/plus-one/#/description
difficulty: easy
"""


class Solution(object):

    def plusOne(self, digits):

        carry = 0

        result = list()

        for index, digit in enumerate(digits[::-1]):

            if not index:

                total = digit + carry + 1

            else:

                total = digit + carry

            carry, digit = divmod(total, 10)

            result.append(digit)

        if carry:

            result.append(carry)

        return result[::-1]

