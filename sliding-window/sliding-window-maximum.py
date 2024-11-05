"""
Reference: https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res: list[int] = []
        dq = deque(maxlen=len(nums))
        i = j = 0

        while j < len(nums):
            while dq and nums[dq[-1]] < nums[j]:
                dq.pop()

            dq.append(j)

            if dq[0] < i:
                dq.popleft()

            if (j + 1) >= k:
                res.append(nums[dq[0]])
                i += 1

            j += 1

        return res


result = Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
print(result)
