# Last updated: 6/4/2026, 9:42:02 PM
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                sum+=i
        return sum