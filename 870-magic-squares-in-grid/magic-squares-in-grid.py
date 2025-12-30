class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows,cols=len(grid),len(grid[0])
        res=0

        def magic(r,c):
            #ensure 0 to 9
            values=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if grid[i][j] in values or not(0<= grid[i][j] <= 9):
                        return 0
                    values.add(grid[i][j])
            # row sum check
            for i in range(r,r+3):
                if sum(grid[i][c:c+3])!=15:
                    return 0

            #col sum check
            for i in range(c,c+3):
                if grid[r][i] + grid[r+1][i] + grid[r+2][i] != 15:
                    return 0

            #diagonal sum check
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
            grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return 0

            #no deviation from the conditions
            return 1

        for r in range(rows-2):
            for c in range(cols-2):
                res+=magic(r,c)

        return res

        