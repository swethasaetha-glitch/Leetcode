# Last updated: 6/29/2026, 7:01:19 PM
1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n <= 0:
4            return False
5        while n % 2 == 0:
6            n //= 2
7        while n % 3 == 0:
8            n //= 3
9        while n % 5 == 0:
10            n //= 5
11        return n == 1