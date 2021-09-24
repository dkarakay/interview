count = 0


def merge(arr, left, right, mid):
    n1 = mid - left + 1
    n2 = right - mid

    left_copy = [0] * n1
    right_copy = [0] * n2
    for i in range(0, n1):
        left_copy[i] = arr[left + i]

    for j in range(0, n2):
        right_copy[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    while i < len(left_copy) and j < len(right_copy):

        if left_copy[i] <= right_copy[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = right_copy[j]
            j += 1

        k += 1

    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1

    while j < len(right_copy):
        arr[k] = right_copy[j]
        j += 1
        k += 1
    global count
    count += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, right, mid)


n = int(input())
arr = [int(x) for x in input().split()]

merge_sort(arr, 0, n - 1)
temp = ""
for a in arr:
    temp += str(a) + ' '
print(temp.strip())
print(count)
