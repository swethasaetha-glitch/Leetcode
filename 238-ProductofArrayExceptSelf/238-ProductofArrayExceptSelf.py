# Last updated: 6/17/2026, 12:21:47 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        return nums[-k]