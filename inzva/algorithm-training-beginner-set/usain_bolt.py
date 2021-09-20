# Usain Bolt is a world famous athlete. In his whole career, he broke lots of new records.
# The points he got from the races he entered are given.
# The task is find how many times Usain Bolt broke his own record.

# SampleInput 1
# 5
# 3 7 2 6 8
# SampleOutput 1
# 2
# SampleInput 2
# 5
# 1 2 3 4 5
# SampleOutput 2
# 4

# n = 5
# a = [3, 2, 1, 4, 6]

n = int(input())
a = input().split(' ')

current_max = int(a[0])
record_time = 0

i = 1

while i < n:
    if int(a[i]) > current_max:
        record_time += 1
        current_max = int(a[i])
    i += 1

print(record_time)