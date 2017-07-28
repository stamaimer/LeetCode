# -*- coding: utf-8 -*-

"""
date: 07/28/17
author: stamaimer
source: https://leetcode.com/problems/house-robber/tabs/description
difficulty: easy
"""


class Solution(object):

    def solve(self, nums, index, result):

        if index < 0:

            return 0

        if result[index] >= 0:

            return result[index]

        result[index] = max(nums[index] + self.solve(nums, index - 2, result), self.solve(nums, index - 1, result))

        return result[index]

    def rob(self, nums):

        result = [-1 for _ in range(len(nums))]

        return self.solve(nums, len(nums) - 1, result)
