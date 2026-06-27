# Last updated: 6/27/2026, 10:21:47 AM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
4        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
5        ans = ""
6        for i in range(len(values)):
7            while num >= values[i]:
8                ans += symbols[i]
9                num -= values[i]
10        return ans