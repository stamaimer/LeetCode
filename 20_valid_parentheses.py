# -*- coding: utf-8 -*-

"""
date: 07/25/17
author: stamaimer
source: https://leetcode.com/problems/valid-parentheses/#/description
difficulty: easy
"""


class Solution(object):

    def isValid(self, s):

        match = dict([(')', '('), ('}', '{'), (']', '[')])

        stack = []

        for char in s:

            if char in match.values():

                stack.append(char)

            else:

                if char in match and stack and match[char] == stack[-1]:

                    stack.pop()

                else:

                    return bool(0)

        return not stack

if __name__ == '__main__':

    print Solution().isValid("()")
