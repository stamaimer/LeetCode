# -*- coding: utf-8 -*-

"""
date: 07/26/17
author: stamaimer
source: https://leetcode.com/problems/find-duplicate-file-in-system/#/description
difficulty: medium
"""


import re
from collections import defaultdict


class Solution(object):

    def findDuplicate(self, paths):

        content2path = defaultdict(list)

        regex = re.compile("(.*)\((.*)\)")

        for item in paths:

            path, *files = item.split()

            for element in files:

                match = re.search(regex, element)

                filename = match.group(1)

                content = match.group(2)

                content2path[content].append('/'.join([path, filename]))

        return [value for value in content2path.values() if len(value) > 1]


if __name__ == "__main__":

    Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"])