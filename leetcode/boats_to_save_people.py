# https://leetcode.com/problems/boats-to-save-people/

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        j = len(people) - 1
        i = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                boat += 1
                j -= 1
                i += 1
            else:
                boat += 1
                j -= 1
        return boat


s = Solution()
print(s.numRescueBoats([3,5,3,4], 5))
