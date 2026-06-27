# Last updated: 6/27/2026, 11:37:54 AM
1class Solution:
2    def countPrimes(self, n: int):
3
4        if n <= 2:
5            return 0
6
7        prime = [True] * n
8        prime[0] = prime[1] = False
9
10        for i in range(2, int(n ** 0.5) + 1):
11
12            if prime[i]:
13
14                for j in range(i * i, n, i):
15                    prime[j] = False
16
17        return sum(prime)