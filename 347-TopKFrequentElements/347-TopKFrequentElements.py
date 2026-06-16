# Last updated: 6/16/2026, 5:23:53 PM
1from collections import Counter
2
3class Solution:
4    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
5        return list(dict(Counter(nums).most_common(k)).keys())