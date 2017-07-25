# -*- coding: utf-8 -*-

"""
date: 07/25/17
author: stamaimer
source: https://leetcode.com/problems/count-and-say/#/description
difficulty: easy
"""


import time

from itertools import groupby


class Solution(object):

    def countAndSay(self, n):

        if n == 1:

            return '1'

        origin_str = "1 "

        result_str = ''

        for _ in range(2, n + 1):

            temp_list = list()

            for c in origin_str:

                if not temp_list or c == temp_list[-1]:

                    temp_list.append(c)

                else:

                    result_str = result_str + str(len(temp_list)) + temp_list[0]

                    temp_list = list()

                    temp_list.append(c)

            origin_str = result_str + ' '

            result_str = ''

        return origin_str[:-1]

    def countAndSayV2(self, n):

        s = '1'

        for _ in range(n - 1):

            s = ''.join(str(len(list(group))) + digit for digit, group in groupby(s))

        return s

if __name__ == '__main__':

    time0 = time.time()

    print Solution().countAndSay(30)

    time1 = time.time()

    print Solution().countAndSayV2(30)

    time2 = time.time()

    print time1 - time0, time2 - time1
