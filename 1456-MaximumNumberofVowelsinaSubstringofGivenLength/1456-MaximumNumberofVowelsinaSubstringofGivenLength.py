# Last updated: 6/29/2026, 6:25:58 PM
1class Solution:
2    def maxVowels(self, s: str, k: int) -> int:
3        count = 0
4
5        # First window
6        for i in range(k):
7            if s[i] in "aeiou":
8                count += 1
9
10        ans = count
11
12        # Slide the window
13        for i in range(k, len(s)):
14            if s[i] in "aeiou":
15                count += 1
16            if s[i-k] in "aeiou":
17                count -= 1
18
19            ans = max(ans, count)
20
21        return ans