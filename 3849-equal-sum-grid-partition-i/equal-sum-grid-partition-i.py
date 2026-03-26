class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        sum = [[0]*(c+1) for _ in range(r+1)]
        total = 0
        for i in range(r):
            for j in range(c):
                sum[i+1][j+1] = (sum[i+1][j]+sum[i][j+1]-sum[i][j]+grid[i][j])

                total += grid[i][j]
        
        for i in range(r-1):
            if total == sum[i+1][c] * 2:
                return True
        for i in range(c-1):
            if total == sum[r][i+1] * 2:
                return True
        return False