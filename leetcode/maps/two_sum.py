# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = {}

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in solution:
                return [solution[pair], i]
            solution[nums[i]] = i

        return []


s = Solution()
print(s.twoSum([2, 7, 8, 12], 9))
