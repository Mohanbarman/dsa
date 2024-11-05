"""
Reference: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (res_r - res_l + 1):
                    res_l = l
                    res_r = r
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > (res_r - res_l + 1):
                    res_l = l
                    res_r = r
                l -= 1
                r += 1

        return s[res_l : res_r + 1]


print(Solution().longestPalindrome("babad"))
