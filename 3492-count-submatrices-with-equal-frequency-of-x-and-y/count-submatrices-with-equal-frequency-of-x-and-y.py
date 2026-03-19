class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])

        count=0

        cx = [[0]*c for _ in range(r)]
        cy = [[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):

                if grid[i][j]=='X':
                    cx[i][j] +=1
                if grid[i][j]=='Y':
                    cy[i][j] +=1

                if i-1>=0:
                    cx[i][j] += cx[i-1][j]
                    cy[i][j] += cy[i-1][j]
                if j-1>=0:
                    cx[i][j] += cx[i][j-1]
                    cy[i][j] += cy[i][j-1]

                if i-1>=0 and j-1>=0:
                    cx[i][j] -= cx[i-1][j-1]
                    cy[i][j] -= cy[i-1][j-1]

                if cx[i][j]>0 and cx[i][j]==cy[i][j]:
                    count+=1


        return count