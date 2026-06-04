# Last updated: 6/4/2026, 9:42:13 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_c=0
        for i  in sentences:
            a=i.split(" ")
            max_c=max(max_c,len(a))
        return max_c
        