# Last updated: 6/4/2026, 9:42:10 PM
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i==i[::-1]:
                return i
        return ""
