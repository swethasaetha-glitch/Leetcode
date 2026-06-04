# Last updated: 6/4/2026, 9:42:28 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1
