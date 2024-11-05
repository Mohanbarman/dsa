"""
Reference: https://leetcode.com/problems/maximum-average-subarray-i/description/
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_average = 0

        for i in range(k):
            cur_average += nums[i]

        i = 0
        j = k
        res = cur_average

        while (j < len(nums)):
            cur_average += nums[j] - nums[i] 
            res = max(cur_average, res)
            i += 1
            j += 1

        return res / k


result = Solution().findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)

