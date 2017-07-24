# -*- coding:utf-8 -*-

"""
date: 07/24/17
author: stamaimer
source: https://leetcode.com/problems/two-sum/#/description
difficulty: easy
"""


class Solution(object):

    excepted_index = dict()

    for idx, num in enumerate(nums):

        if num in excepted_index:

            return excepted_index[num], idx

        else:

            excepted_index[target - num] = idx

