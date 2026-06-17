# Last updated: 6/17/2026, 11:38:29 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        d={}
4        for i in strs:
5            s="".join(sorted(i))
6            if s not in d:
7                d[s]=[i]
8            else:
9                d[s].append(i)
10        return list(d.values())