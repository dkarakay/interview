# https://leetcode.com/problems/count-primes/
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [False, False]
        if n < 2:
            return 0

        for i in range(n - 2):
            prime.append(True)

        i = 2
        while i <= int(math.sqrt(n)):
            if prime[i]:
                for multiples in range(i * i, n, i):
                    prime[multiples] = False
            i += 1
        return sum(prime)


s = Solution()
print(s.countPrimes(0))
