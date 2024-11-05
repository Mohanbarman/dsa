class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while (l <= r):
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res


input_arr = [45, 45, 345, 2345, 0, 2, 3, 4, 5, 5, 23, 23, 26]
print(Solution().findMin(input_arr))
