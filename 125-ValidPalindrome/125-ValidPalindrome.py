# Last updated: 6/4/2026, 9:42:47 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=s.lower()
        f=""
        for i in a:
            if i.isalnum():
                f+=i
        return f==f[::-1]