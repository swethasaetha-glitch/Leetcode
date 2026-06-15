# Last updated: 6/15/2026, 9:31:30 PM
1class Solution:
2    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
3        possible = {0}
4        for i in range(len(s)):
5            if i in possible:
6                for word in wordDict:
7                    if s.startswith(word, i):
8                        possible.add(i + len(word))
9
10        return len(s) in possible