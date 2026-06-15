# Last updated: 6/15/2026, 9:50:37 PM
1class Solution:
2    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
3        ans=[]
4        for i,words in enumerate(words):
5            if x in words:
6                ans.append(i)
7        return ans