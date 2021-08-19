# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max_area = 0
        while left < right:
            max_area = max(min(height[left], height[right]) * (right - left), max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
