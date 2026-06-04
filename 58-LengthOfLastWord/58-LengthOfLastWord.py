# Last updated: 6/4/2026, 9:42:58 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.strip().split()
        return len(a[-1])
