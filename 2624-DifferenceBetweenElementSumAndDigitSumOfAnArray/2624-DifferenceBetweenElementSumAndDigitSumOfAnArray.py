# Last updated: 6/4/2026, 9:42:07 PM
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums)- sum(int(d) for i in nums for d in str(i)))