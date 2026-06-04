# Last updated: 6/4/2026, 9:42:36 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)