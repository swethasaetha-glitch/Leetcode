# Last updated: 6/9/2026, 2:26:03 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen=set()
4        while n!=1:
5            if n in seen:
6                return False
7            seen.add(n)
8            digits=str(n)
9            t=0
10            for i in digits:
11                t+=int(i)**2
12            n=t
13        return True