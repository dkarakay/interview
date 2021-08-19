# https://leetcode.com/problems/first-bad-version/submissions/

class Solution:
    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return an integer
    # def isBadVersion(version):

    def first_better(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid) == True:
                right = mid - 1
            else:
                left = mid + 1
        return left


def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid
            right = mid - 1
        else:
            left = mid + 1

    print(isBadVersion(4))
