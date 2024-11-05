"""
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        i = 0
        j = 0
        visited = set()

        while j < len(s):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1

            res = max(j - i + 1, res)
            visited.add(s[j])
            j += 1

        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))
