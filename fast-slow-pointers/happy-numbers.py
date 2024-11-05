"""
Reference: https://leetcode.com/problems/happy-number/submissions/1440649735/
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = self.calcHappy(n)

        while fast != 1:
            slow = self.calcHappy(slow)
            fast = self.calcHappy(self.calcHappy(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False

        return True

    def calcHappy(self, n: int):
        res = 0
        num = n
        while num > 0:
            res += (num % 10) * (num % 10)
            num //= 10

        return res


print(Solution().isHappy(13))
