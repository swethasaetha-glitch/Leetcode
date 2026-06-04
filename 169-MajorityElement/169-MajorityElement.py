# Last updated: 6/4/2026, 9:42:39 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]