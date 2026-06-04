# Last updated: 6/4/2026, 9:43:05 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]=sorted(set(nums))
        return len(nums)