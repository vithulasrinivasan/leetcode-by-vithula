class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r , c = len(grid) , len(grid[0])
        count =0
        for x in range(r):
            for y in range(c):
                if x-1 >=0:
                    grid[x][y] += grid[x-1][y]
                if y-1 >=0:
                    grid[x][y] += grid[x][y-1]
                if x-1 >=0 and y-1>=0 :
                    grid[x][y] -= grid[x-1][y-1]

                if grid[x][y] <= k :
                    count+=1
        return count
