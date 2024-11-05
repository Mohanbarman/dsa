"""
Reference: https://leetcode.com/problems/minimum-window-substring/description/
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 1 and len(t) == 1 and s != t:
            return ""
        if len(t) > len(s):
            return ""

        t_occurence = {}
        for c in t:
            if c in t_occurence:
                t_occurence[c] += 1
            else:
                t_occurence[c] = 1

        i = 0
        j = 0
        res = None
        s_occurence = {}

        while j < len(s):
            if s[j] in s_occurence:
                s_occurence[s[j]] += 1
            else:
                s_occurence[s[j]] = 1

            while i < len(s) and (
                s[i] not in t_occurence
                or (s[i] in s_occurence and t_occurence[s[i]] < s_occurence[s[i]])
            ):
                if s[i] in s_occurence:
                    s_occurence[s[i]] -= 1
                i += 1

            valid_substr = True
            for key, value in t_occurence.items():
                if key not in s_occurence or s_occurence[key] < value:
                    valid_substr = False
                    break

            if valid_substr:
                cur_substr_len = j - i + 1
                if res is None:
                    res = (i, j)
                prev_substr_len = res[1] - res[0] + 1
                if cur_substr_len < prev_substr_len:
                    res = (i, j)

            j += 1

        if res is None:
            return ""
        return s[res[0] : res[1] + 1]

    def minWindow2(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_occurence = {}
        for i in t:
            if i in t_occurence:
                t_occurence[i] += 1
            else:
                t_occurence[i] = 1

        i = 0
        j = 0
        count = len(t_occurence)
        min_size = float('inf')
        min_start = 0

        while j < len(s):
            if s[j] in t_occurence:
                t_occurence[s[j]] -= 1
                if t_occurence[s[j]] == 0:
                    count -= 1

            while count == 0:
                cur_min_size = min(j - i + 1, min_size)
                if cur_min_size < min_size:
                    min_start = i
                    min_size = cur_min_size
                if s[i] in t_occurence:
                    t_occurence[s[i]] += 1
                    if t_occurence[s[i]] > 0:
                        count += 1
                i += 1

            j += 1

        if min_size == float('inf'):
            return ""

        return s[min_start : min_start + min_size]


# result = Solution().minWindow2("ADOBECODEBANC", "ABC")
result = Solution().minWindow2("aa", "aa")
# result = Solution().minWindow("ab", "A")
print(result)
