# New stickers have arrived at inzva Sanctuary. But not enough stickers for every participant.
# So, Havva decides to ask a question to participants and give a sticker for the right answer. Havva gives the number N
# to participants asks them to multiply all the digits except zeros.
# Then asks them to apply the same operation to the result, until only one digit left.
# The right answer is just that number.
# Yasin really wants those stickers, can you help Yasin to get a sticker?

# Sample Input 1
# 366
# Sample Output 1
# 8
# Explanation 1
# 3 * 6 * 6 = 108 1 * 8 = 8
# answer is 8
# Sample Input 2
# 157007997196592516
# Sample Output 2
# 2

number = int(input())


def multiplier(number):
    if number < 10:
        return number

    result = 1
    for c in str(number):
        if int(c) != 0:
            result *= int(c)

    return multiplier(result)


print(multiplier(number))
