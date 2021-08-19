# https://leetcode.com/problems/valid-mountain-array/
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        i = 0
        ind1 = -1
        ind2 = -1
        j = len(arr) - 1
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1] or arr[j] == arr[j - 1]:
                return False
            if arr[i] > arr[i + 1] and ind1 == -1:
                ind1 = i
            if arr[j] > arr[j - 1] and ind2 == -1:
                ind2 = j
            i += 1
            j -= 1
        if ind1 != ind2:
            return False
        return True

    def valid_mountain(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        i = 0
        while i < len(arr)-1 and arr[i] < arr[i+1]:
            i += 1

        if i == 0 or i == len(arr)-1:
            return False

        while i < len(arr)-1 and arr[i] > arr[i+1]:
            i += 1

        return i == len(arr)-1


s = Solution()
print(s.valid_mountain([2,0,2]))
