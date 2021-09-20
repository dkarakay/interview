# One day, Omar and Havva went to the ice cream shop. There are N different types of ice cream and the shop has Ai
# kilogram of each type. Omar wants to eat lots of ice cream, therefore he decided to eat all of the
# N−1 types of ice cream and leave one type to Havva. Since he wants to eat lots of ice cream,
# could you print the maximum amount of ice cream that Omar can eat?

# Input Format
# The first line contains one integer, N
# The next line contains N integers, Ai - the amount of ice cream of type i

# SampleInput 1
# 8
# 10 3 8 9 7 5 5 5

# SampleOutput 1
# 49

# SampleInput 2
# 2
# 5 10

# SampleOutput 2
# 10

n = int(input())
a = [int(x) for x in input().split(' ')]

print(sum(a) - sorted(a)[0])
