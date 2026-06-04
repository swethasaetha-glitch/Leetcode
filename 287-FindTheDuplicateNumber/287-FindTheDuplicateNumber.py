# Last updated: 6/4/2026, 9:42:33 PM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i in s:
                return i
            s.add(i)
