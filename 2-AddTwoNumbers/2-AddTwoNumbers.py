# Last updated: 6/30/2026, 1:49:11 PM
1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        r=0
4        for i in columnTitle:
5            r=r*26+(ord(i)-ord('A')+1)
6        return r