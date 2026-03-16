class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        def get_sum(x,y,l):
            if l==0:
                return grid[x][y]
            
            cx,cy = x-l , y #top corner of the rhombus
            total=0
            for dx,dy in [[1,1],[1,-1],[-1,-1],[-1,1]]:
                for _ in range(l):
                    cx += dx
                    cy += dy
                    total += grid[cx][cy]
            return total


        vals = SortedSet()

        r=len(grid) # rows
        c=len(grid[0]) # cols

        # rhombus center at x,y
        for x in range(r):
            for y in range(c):
                l=0 # width
                while x+l<r and y+l<c and x-l>=0 and y-l>=0:
                    summ=get_sum(x,y,l)
                    vals.add(summ)
                    if len(vals)>3:
                        vals.remove(vals[0])
                    l+=1

        return list(reversed(vals))
