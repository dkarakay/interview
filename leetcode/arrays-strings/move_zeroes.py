# https://leetcode.com/problems/move-zeroes/


def moveZeroes(nums: list[int]) -> None:
    j = 0
    for ind, val in enumerate(nums):
        if val != 0:
            nums[j] = val
            j += 1
    for i in range(len(nums)-j):
        nums[j+i] = 0

    print(nums)


L = [0,0,1]
moveZeroes(L)
