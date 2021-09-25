# Fehmi is playing a different version of hopscotch that consists of n rows.
# His hopscotch is described with numbers in each row, starting from the lowest:
# 1 - (2,3) - 4 - (5,6) - 7 ...
# s a general rule, number of squares in the rows of hopscotch forms a pattern of
# 1 − 2 − 1 − 2 − 1 − 2
# Fehmi is extremely good in this game. He will make k jumps. In his first jump,
# Fehmi will jump to the first row, and then in each jump, Fehmi will jump to the next row. If he is already at
# nth row (at the end of the rows), in the next jump he will turn back and jump to
# (n−1)th row back. Also, when he turns back to the first row,
# he will again turn back to second row and continue to jump until the kth jump.
# Your task is the print out the numbers at the row that Fehmi will be located at after k jumps.

i = 1
input_l = input().split(' ')

n = int(input_l[0])
step = int(input_l[1])

while step >= (n - 1) * 2:
    step -= (n - 1) * 2

mod = step % ((n - 1) * 2)
if mod == 0:
    mod = ((n - 1) * 2)

if mod > n:
    mod = (n * 2) - mod

if mod % 2 == 0:
    x = (mod // 2) - 1
    print(f"{mod + x} {mod + 1 + x}")
else:
    x = mod // 2
    print(x + mod)
