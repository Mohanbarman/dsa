"""
You are given a string 'str' and an integer ‘K’. Your task is to find the length of the largest substring with at most ‘K’ distinct characters.

For example:
You are given ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 10
1 <= K <= 26
1 <= |str| <= 10^6

The string str will contain only lowercase alphabets.    

Time Limit: 1 sec
Note:
You do not need to print anything. It has already been taken care of. Just implement the function.
Sample Input 1:
2
2
abbbbbbc
3
abcddefg
Sample Output 1:
7
4
Explanation:
For the first test case, ‘str’ = ‘abbbbbbc’ and ‘K’ = 2, then the substrings that can be formed are [‘abbbbbb’, ‘bbbbbbc’]. Hence the answer is 7.

For the second test case, ‘str’ = ‘abcddefg’ and ‘K’ = 3, then the substrings that can be formed is [‘cdde’, ‘ddef’]. Hence the answer is 4.
Sample Input 2:
2
3
aaaaaaaa
1
abcefg
Sample Output 2:
8   
1   

Ref: https://www.naukri.com/code360/problems/distinct-characters_2221410
"""


def solve(s: str, k: int):
    occurences = {}
    i = 0
    j = 0
    res = 0

    while j < len(s):
        if s[j] in occurences:
            occurences[s[j]] += 1
        else:
            occurences[s[j]] = 1

        while len(occurences) > k:
            occurences[s[i]] -= 1
            if occurences[s[i]] < 1:
                occurences.pop(s[i])
            i += 1

        if len(occurences) == k:
            res = max(j - i + 1, res)

        j += 1

    if res == 0:
        return len(s)

    return res


print(solve("abbbbbbc", 2))
print(solve("abcddefg", 3))
print(solve("aaaaaaaa", 1))
print(solve("abcefg", 1))
