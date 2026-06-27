# Last updated: 6/27/2026, 10:14:19 AM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
4
5        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
6
7        ans = ""
8
9        for i in range(len(values)):
10
11            while num >= values[i]:
12                ans += symbols[i]
13                num -= values[i]
14
15        return ans