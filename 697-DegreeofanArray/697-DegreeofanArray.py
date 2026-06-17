# Last updated: 6/17/2026, 10:16:19 AM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        nums1[m:] = nums2
4        nums1.sort()
5        