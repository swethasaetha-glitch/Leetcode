# Last updated: 6/22/2026, 11:30:48 AM
1class Solution:
2    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        pos = {num: i for i, num in enumerate(nums)}
6        sorted_nums = sorted(nums)
7
8        bit = [0] * (n + 1)
9
10        def update(i, val):
11            i += 1
12            while i <= n:
13                bit[i] += val
14                i += i & -i
15
16        def query(i):
17            s = 0
18            i += 1
19            while i > 0:
20                s += bit[i]
21                i -= i & -i
22            return s
23
24        for i in range(n):
25            update(i, 1)
26
27        ans = 0
28        curr = 0
29
30        for num in sorted_nums:
31            idx = pos[num]
32
33            if idx >= curr:
34                ans += query(idx) - query(curr - 1)
35            else:
36                ans += (query(n - 1) - query(curr - 1))
37                ans += query(idx)
38
39            update(idx, -1)
40            curr = idx
41
42        return ans