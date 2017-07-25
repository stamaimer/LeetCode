# -*- coding:utf-8 -*-

"""
date: 07/23/17
author: stamaimer
source: https://leetcode.com/problems/total-hamming-distance/#/description
difficulty: medium
"""


class Solution(object):

    def totalHammingDistance(self, nums):

        result = 0

        for i, num_a in enumerate(nums):

            for num_b in nums[i + 1:]:

                binary_a = "{0:032b}".format(num_a)
                binary_b = "{0:032b}".format(num_b)

                result += [int(a) ^ int(b)
                           for a, b in zip(binary_a, binary_b)].count(1)
        return result

    def totalHammingDistanceV2(self, nums):

        result = 0

        binaries = ["{0:032b}".format(num) for num in nums]

        for i, binary_a in enumerate(binaries):

            for binary_b in binaries[i + 1:]:

                result += [int(a) ^ int(b) for a, b in zip(binary_a, binary_b)].count(1)

        return result

    def totalHammingDistanceV3(self, nums):

        return sum(column.count('1') * column.count('0') for column in zip(*map("{0:032b}".format, nums)))
