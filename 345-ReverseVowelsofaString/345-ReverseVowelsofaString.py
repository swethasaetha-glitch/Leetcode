# Last updated: 6/16/2026, 2:15:10 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        vow="aeiouAEIOU"
4        v=[]
5        for i in s:
6             if i in vow:
7                v.append(i)
8        ans=""
9        for i in s:
10            if i in vow:
11                ans+=v.pop()
12            else:
13                ans+=i
14        return ans