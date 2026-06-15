# Last updated: 6/15/2026, 9:30:09 AM
1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        ans = int(dividend / divisor)
4
5        MAX_INT = 2**31 - 1
6        MIN_INT = -2**31
7
8        if ans > MAX_INT:
9            return MAX_INT
10        if ans < MIN_INT:
11            return MIN_INT
12
13        return ans