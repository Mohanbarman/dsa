class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        min_index = 0

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < nums[min_index]:
                    min_index = l
                break

            mid = (l + r) // 2
            if nums[mid] < nums[min_index]:
                min_index = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        if min_index == 0:
            return self.binary_search(nums, 0, len(nums) - 1, target)
        if target > nums[-1]:
            return self.binary_search(nums, 0, min_index - 1, target)
        return self.binary_search(nums, min_index, len(nums) - 1, target)

    def binary_search(self, nums: list[int], left: int, right: int, target: int) -> int:
        l = left
        r = right

        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
