# Last updated: 6/30/2026, 12:31:37 PM
1class Solution:
2    def checkXMatrix(self, grid: List[List[int]]) -> bool:
3        n = len(grid)
4
5        for i in range(n):
6            for j in range(n):
7
8                if i == j or i + j == n - 1:
9                    if grid[i][j] == 0:
10                        return False
11                else:
12                    if grid[i][j] != 0:
13                        return False
14
15        return True