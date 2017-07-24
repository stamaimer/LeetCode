# -*- coding: utf-8 -*-

"""
date: 07/24/17
author: stamaimer
source: https://leetcode.com/problems/longest-common-prefix/#/description
difficulty: easy
"""


class Solution(object):

    def longestCommonPrefix(self, strs):

        result_str = ''

        if strs and all(str):

            result_idx = [index if len(set(column)) == 1 else -1 
                          for index, column in enumerate(zip(*strs))]

            for index in result_idx:

                if index == -1:

                    break

                else:

                    result_str += strs[0][index]

        return result_str

