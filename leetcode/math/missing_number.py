# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum = int((n * (n + 1)) / 2)

        for val in nums:
            sum -= val

        return sum


s = Solution()
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
