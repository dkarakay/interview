def find_closest(smaller, larger, ind_small, ind_large, target):
    return ind_large if target - smaller >= larger - target else ind_small


def get_closer(arr: list, target: int):
    left = 0
    right = len(arr) - 1
    mid = 0

    if target > arr[-1]:
        return arr[-1]

    if target < arr[0]:
        return arr[0]

    while left < right:
        mid = (left + right) // 2

        if target > arr[mid]:
            left = mid + 1
        elif target < arr[mid]:
            right = mid

            #return mid, -1

    # value = arr[mid]
    # low = mid if value < key else mid - 1
    # up = mid if value > key else mid + 1

    return (left - 1, left)

    # if target < arr[mid]:
    #    return find_closest(arr[mid - 1], arr[mid], mid - 1, mid, target)
    # else:
    #    return find_closest(arr[mid], arr[mid + 1], mid, mid + 1, target)


n, k = [int(x) for x in input().split(' ')]
games = input().split(' ')
game_prices = []
test = []

for game in games:
    if game != '':
        game_prices.append(int(game))

q = int(input())

for g in range(q):
    test.append(int(input()))

for val in test:
    min_range = k - val
    max_range = k + val
    print(f"{min_range} - {max_range}")

    if min_range < game_prices[0] and game_prices[-1] < max_range:
        print(len(game_prices))
        continue
    elif min_range < game_prices[0] and game_prices[-1] > max_range:
        # max_index = get_closer(game_prices, max_range)
        # print(max_index)
        continue
    elif min_range > game_prices[0] and game_prices[-1] < max_range:
        # min_index = get_closer(game_prices, min_range)
        # print(min_index)
        continue
    else:
        lower, upper = get_closer(game_prices, min_range)
        print(f"{val}: {lower} - {upper}")
        # max_index = get_closer(game_prices, max_range)
        # print(f"{min_index} - {max_index} -> {abs(max_index - min_index + 1)}")

    # print(f"{val} ->> {abs(max_index - min_index + 1)}")
