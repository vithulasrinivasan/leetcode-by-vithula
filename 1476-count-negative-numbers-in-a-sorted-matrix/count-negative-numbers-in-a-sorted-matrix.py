class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        negative=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]<0:
                    negative+=1
        return negative