# -*- coding: utf-8 -*-

"""
date: 08/23/17
author: stamaimer
source: https://leetcode.com/problems/range-sum-query-immutable/description
difficulty: easy
"""


class NumArray(object):

    def __init__(self, nums):

        for index in range(1, len(nums)):

            nums[index] += nums[index - 1]

        self.nums = nums

    def sumRange(self, i, j):

        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]
