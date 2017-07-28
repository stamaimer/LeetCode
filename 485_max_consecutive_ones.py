# -*- coding: utf-8 -*-

"""
date: 07/28/17
author: stamaimer
source: https://leetcode.com/problems/max-consecutive-ones/tabs/description/
difficulty: easy
"""


class Solution(object):

    def findMaxConsecutiveOnes(self, nums):

        if any(nums):

            return len(max((item for item in ''.join(map(str, nums)).split('0') if item), key=len))

        else:

            return 0
