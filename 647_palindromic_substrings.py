# -*- coding: utf-8 -*-

class Solution(object):
    def is_palindromic(self, string, temp_dict):

        # if string in temp_dict:
        #     return temp_dict[string]

        length = len(string)

        for i in range(length / 2):

            if string[i] != string[-1 - i]:
                temp_dict[string] = 0

                break
        else:

            temp_dict[string] = 1

        return temp_dict[string]

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0

        temp = ''

        temp_dict = dict()

        for idx, x in enumerate(s):

            temp = x

            count += 1

            for y in s[idx + 1:]:

                temp += y

                if self.is_palindromic(temp, temp_dict):
                    count += 1

        return count

if __name__ == '__main__':

    print Solution().countSubstrings("dbabcccbcdbbbadabbdabaabcbbabaacdadcdbbbbdddbcbbbcbcabacacdaadaadcdccbacdaadadcbaacabbddabdadcabbccadacadaaacbbddaaababacaabbbacaccbcbbabddbbcccaaacbcdcabcbacdbddcdcadaaadcbccbbcabbcbdaadcbddaacacdadacbbdabcdcdadccaccdbdddddcabdbcdbaadacadadbabdcdbbadaacdbadcdabdbbcabbbdaacaaaaadcaabaaaadabaaddcaabdddcbcadcbdbbdbcbcdbadcadacbbcdccddaccccacbacaacbbdadadcacabdabadbbcdbcaaccdbdcabcadbacbccddbabbdacbcbbcbcabcacdaacccaadcdbdccabcaaacaddadcabacdccaaaddaaadbccdbbcccdddababcdbcddcbdddbbbdaadaccbcaabbcbdbadbabbacdbbbdaaccdcabddacadabcccacdabacbcdbcbdabddacacbdbcaacacaabbaaccddabaadbbaabaddbcacbacdbbbacdccabbcdbbbdbdbbcacabdddbdbaaabbcdcbabcbbbccdcdcdcaaddadccbabbacaddcaddcadcdccaccacabbaababdbbcbdcdccccccdadbdbdcdbdadcdcacdaabaacabaacdacdbaaccadbcddbdccabbcabcadcbdadbcdadbbbccacbcbbcaaaabdacbadacaadcadaacdacddcbbabdacacaabccdaccbbcbbcbcaacdabdcbcdbccdbcbcbddaacdacaaaddcaddcadccacbaddbbbccbbbcbbcbadcabbccbbaadaacacabddbdbddcadbdaaccadbcccabdcdbadbbacbcbbcdcabcddcddddabddbdabdcabdbdbbbcdbcdabbdcb")