# Harun and Sami are very good friends. They play a game for N rounds. In each round, Harun or Sami wins.
# In other words, a round never ends in a draw. To win the game, you need to win more rounds than your opponent.
# Unfortunately, they only remember the result of the first
# K round. Also, both of them claim to have won the game.
# Therefore, you need to determine if anyone has definitely won the game or not by considering the first K round.

# Output Format
# If it is certain that Harun won the game, print "Harun".
# If it is certain that Sami won the game, print "Sami".
# If the winner cannot be determined from the results of the first K rounds, print "Cilek".

# Sample Input 1
# 7 5
# HSHHH
# Sample Output 1
# Harun
# Sample Input 2
# 7 5
# HSHSH
# Sample Output 2
# Cilek
input_l = input().split(' ')

n = int(input_l[0])
k = int(input_l[1])

s = input()

sami = 0
harun = 0

for c in s:
    if c == 'S':
        sami += 1
    elif c == 'H':
        harun += 1

diff = n - k
dif = abs(sami - harun)

if sami > harun and dif > diff:
    print("Sami")
elif harun > sami and dif > diff:
    print("Harun")
elif sami == harun and dif == diff:
    print("Cilek")
else:
    print("Cilek")
