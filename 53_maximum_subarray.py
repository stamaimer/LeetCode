# -*- coding: utf-8 -*-

"""
date: 08/03/17
author: stamaimer
source: https://leetcode.com/problems/maximum-subarray/description/
difficulty: easy
"""


class Solution(object):

    def maxSubArray(self, nums):

        answer = -float("inf")

        for i in range(len(nums)):

            for j in range(i, len(nums)):

                total = 0

                for k in range(i, j + 1):

                    total += nums[k]

                answer = max(answer, total)

        return answer

    def maxSubArrayV2(self, nums):

        answer = -float("inf")

        for i in range(len(nums)):

            total = 0

            for j in range(i, len(nums)):

                total += nums[j]

                answer = max(answer, total)

        return answer

    def maxSubArrayV3(self, nums):

        answer = -float("inf")

        total = 0

        for i in range(len(nums)):

            total += nums[i]

            answer = max(answer, total)

            if total < 0:

                total = 0

        return answer
