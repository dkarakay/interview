# https://www.youtube.com/watch?v=I0O0Ul65Cgo&list=PLhnxo6HZwBglbALWurJhkVMCGkgtamhXj&index=11

def binarySearch(arr, l, r, x):
    while r >= l:

        mid = l + (r - l) // 2
        print(f"{mid + 1} {arr[mid]}")

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            r = mid - 1

        else:
            l = mid + 1

    return -1


target = int(input())

# result = binary_search(target=target, left=1, right=1024)

arr = []
for i in range(1024):
    arr.append(int(input()))
result = binarySearch(arr=arr, l=0, r=1023, x=target)
