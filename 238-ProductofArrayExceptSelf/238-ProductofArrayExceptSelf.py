# Last updated: 6/17/2026, 12:08:56 PM
1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        return len(s)==len(goal) and goal in (s+s)