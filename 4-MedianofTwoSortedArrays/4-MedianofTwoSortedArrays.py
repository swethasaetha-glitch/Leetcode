# Last updated: 6/29/2026, 6:38:34 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        arr=nums1+nums2
4        arr.sort()
5        n=len(arr)
6        if n%2==1:
7            return arr[n//2]
8        else:
9            return (arr[n//2]+arr[n//2-1])/2