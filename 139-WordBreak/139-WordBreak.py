# Last updated: 6/15/2026, 9:21:01 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        memo = {}
4
5        def solve(start):
6            if start == len(s):
7                return True
8
9            if start in memo:
10                return memo[start]
11
12            for word in wordDict:
13                if s.startswith(word, start):
14                    if solve(start + len(word)):
15                        memo[start] = True
16                        return True
17
18            memo[start] = False
19            return False
20
21        return solve(0)