# Strange things are happening in inzva.
# The word machine that causes these strange things is destroying the words that are new to inzva.
# If identical letters are consecutive, this machine deletes consecutive and identical letters of a received word,
# leaving only one of the identical letters.
# In other words, identical characters will not be consecutive in the arranged word.
# Your task is to print the final version of the word that was changed by the machine.

# SampleInput 1
# 9
# SSSVEEEJJ
# SampleOutput 1
# SVEJ
# SampleInput 2
# 4
# AAAA
# SampleOutput 2
# A

n = int(input())
s = input()

output = ''

i = 0
j = 1

while i < len(s) and j < len(s):
    if s[i] == s[j]:
        j += 1
    else:
        output += s[i]
        i = j
        j += 1

output += s[-1]
print(output)
