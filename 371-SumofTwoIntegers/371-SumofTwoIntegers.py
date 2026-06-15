# Last updated: 6/15/2026, 11:50:46 AM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        return len(nums) != len(set(nums))