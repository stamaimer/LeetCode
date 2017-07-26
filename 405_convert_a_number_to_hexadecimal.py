# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/convert-a-number-to-hexadecimal/#/description
difficulty: easy
"""


class Solution(object):

    def toHex(self, num):

        bin2hex = dict([("0000", '0'), ("0001", '1'), ("0010", '2'), ("0011", '3'),
                        ("0100", '4'), ("0101", '5'), ("0110", '6'), ("0111", '7'),
                        ("1000", '8'), ("1001", '9'), ("1010", 'a'), ("1011", 'b'),
                        ("1100", 'c'), ("1101", 'd'), ("1110", 'e'), ("1111", 'f')])

        binary = ''

        if num < 0:

            binary = "{0:032b}".format(int(''.join('0' if bit == '1' else '1' for bit in "{0:032b}".format(-num)), 2) + 1)

        else:

            binary = bin(num)[2:]

        result = ''

        for i in range(len(binary) - 4, -4, -4):

            chunk = binary[i if i > 0 else 0: i + 4]

            length = len(chunk)

            if length != 4:

                chunk = chunk.zfill(4)

            result += bin2hex[chunk]

        return reversed(result)


if __name__ == '__main__':

    Solution().toHex(-1)