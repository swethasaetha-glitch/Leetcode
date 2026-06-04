# Last updated: 6/4/2026, 9:42:18 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x*x for x in nums])