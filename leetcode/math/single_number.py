# https://leetcode.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sum_of_nums = sum(nums)

        nums_set = set(nums)

        for i in nums_set:
            sum_of_nums -= (2 * i)

        return -1 * sum_of_nums

    # Alternative
    def single_number(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sum_of_nums = 2 * sum(set(nums)) - sum(nums)

        return sum_of_nums


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
