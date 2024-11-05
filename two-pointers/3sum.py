class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = value + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
