# Last updated: 6/27/2026, 11:49:01 AM
1class Solution:
2    def countPrimes(self, n: int):
3        if n <= 2:
4            return 0
5
6        prime = [True] * n
7
8        prime[0] = False
9        prime[1] = False
10
11        for i in range(2, n):
12
13            if prime[i]:
14
15                for j in range(i * 2, n, i):
16                    prime[j] = False
17
18        return prime.count(True)