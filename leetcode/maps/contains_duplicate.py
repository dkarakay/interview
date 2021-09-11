# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicate_maps(self, nums: List[int]) -> bool:
        num_dict = {}

        for num in nums:
            if num in num_dict:
                return True
            num_dict[num] = True

        return False



s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
