# Last updated: 6/9/2026, 2:12:09 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        if x < 0:
4            rev = -int(str(-x)[::-1])
5        else:
6            rev = int(str(x)[::-1])
7
8        if rev < -2**31 or rev > 2**31 - 1:
9            return 0
10
11        return rev