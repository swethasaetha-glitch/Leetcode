# Last updated: 6/16/2026, 10:29:45 PM
1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3        return(word.isupper() or word.islower() or word[0].isupper() and word[1:].islower())