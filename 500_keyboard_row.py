# -*- coding: utf-8 -*-

"""
date: 07/22/17
author: stamaimer
source: https://leetcode.com/problems/keyboard-row/#/description 
difficulty: easy
"""


class Solution(object):

    def findWords(self, words):

        rows = [set("zxcvbnm"), set("asdfghjkl"), set("qwertyuiop")]

        result = list()

        for word in words:

            word_set = set(char.lower() for char in word)

            for row in rows:

                if word_set <= row:  # learn from leetcode
                # if word_set | row == row:  # own implement

                    result.append(word)

                    break

        return result

