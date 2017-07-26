# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/single-number/#/description
difficulty: easy
"""


class Solution(object):

    def singleNumber(self, nums):

        nums.sort()

        for num in nums[1:]:

            if nums[0] is None:

                nums[0] = num

            elif num == nums[0]:

                nums[0] = None

        return nums[0]


if __name__ == '__main__':

    Solution().singleNumber([1, 0, 1])
