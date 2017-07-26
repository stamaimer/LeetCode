# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/rotate-array/#/description
difficulty: easy
"""


class Solution(object):

    def rotate(self, nums, k):

        n = len(nums)

        if k == 0 or k == n:

            return

        nums[: n - k] = reversed(nums[: n - k])
        nums[n - k: ] = reversed(nums[n - k: ])

        nums.reverse()
