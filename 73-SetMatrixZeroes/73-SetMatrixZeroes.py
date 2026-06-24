# Last updated: 6/24/2026, 10:20:54 AM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        rows = len(matrix)
4        cols = len(matrix[0])
5
6        row = [False] * rows
7        col = [False] * cols
8
9        for i in range(rows):
10            for j in range(cols):
11                if matrix[i][j] == 0:
12                    row[i] = True
13                    col[j] = True
14
15        for i in range(rows):
16            for j in range(cols):
17                if row[i] or col[j]:
18                    matrix[i][j] = 0