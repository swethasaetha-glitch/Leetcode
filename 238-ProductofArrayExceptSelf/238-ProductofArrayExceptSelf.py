# Last updated: 6/17/2026, 11:48:47 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        while "()" in s or "{}" in s or "[]" in s:
4            s = s.replace("()", "")
5            s = s.replace("{}", "")
6            s = s.replace("[]", "")
7
8        return s == ""