def binary_search(arr: list, target: int, left, right):
    mid = (left + right) // 2
    temp = []

    print(f"{mid} {mid}")

    if arr[mid] == target:
        return mid
    else:
        if arr[mid] > target:
            for i in range(mid + 1, right):
                temp.append(i)
            return binary_search(temp, target, left=mid + 1, right=right)
        else:
            for i in range(left, mid - 1):
                temp.append(i)

            return binary_search(temp, target, left=left, right=mid - 1)


target = int(input())

arr = []
for i in range(1, 1025):
    arr.append(i)

result = binary_search(arr=arr, target=target, left=1, right=len(arr) - 1)
