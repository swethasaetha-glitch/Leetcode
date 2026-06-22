# Last updated: 6/22/2026, 2:05:43 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        count = 0
4        prefix = 0
5        d = {0: 1}
6
7        for num in nums:
8            prefix += num
9
10            if prefix - k in d:
11                count += d[prefix - k]
12
13            d[prefix] = d.get(prefix, 0) + 1
14
15        return count