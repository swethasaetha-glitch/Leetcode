# Last updated: 7/1/2026, 10:15:22 AM
1class Solution:
2    def reverseWords(self, s: str) -> str:
3        return " ".join(s.split()[::-1])