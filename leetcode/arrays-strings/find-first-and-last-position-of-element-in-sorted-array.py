# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def first_pos(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return -1

    def last_pos(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.first_pos(nums, target)
        last = self.last_pos(nums, target)

        return [first, last]


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
