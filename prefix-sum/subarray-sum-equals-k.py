class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sum_arr = [nums[0]]
        res = 0

        for i in range(1, len(nums)):
            sum_arr.append(sum_arr[-1] + nums[i])

        for i in range(len(nums)):
            if nums[i] == k:
                res += 1
            for j in range(i + 1, len(nums)):
                sub_arr_sum = sum_arr[j] - sum_arr[i - 1]
                if i == 0:
                    sub_arr_sum = sum_arr[j]

                if sub_arr_sum == k:
                    res += 1

        return res
