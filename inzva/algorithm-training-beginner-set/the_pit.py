# List of all binary strings of length N
# Sample Input 1
# 3
# Sample Output 1
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

n = int(input())
i = 0


def binary_strings(n, arr, i):
    if i == n:
        temp = ""
        for x in arr:
            temp += str(x)
        print(temp)
        return
    arr[i] = 0
    binary_strings(n, arr, i + 1)

    arr[i] = 1
    binary_strings(n, arr, i + 1)


arr = [None] * n
binary_strings(n, arr, i)
