class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m,n= col , row
        # Any cell in the top row to any cell in the bottom row
        # DFS - deepest cell first
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]

        def can_cross(day):
            grid = [[0]*m for _ in range(n)]
            for i in range(day):
                x,y = cells[i]
                grid[x-1][y-1] = 1
            visited = [[False]*m for _ in range(n)]

            def dfs(i,j):
                if i==n-1:
                    return True
                visited[i][j]= True
                for dx,dy in dirs:
                    ni, nj = i+dx, j+dy
                    if 0<=ni<n and 0<=nj<m:
                        if not visited[ni][nj] and grid[ni][nj]==0:
                            if dfs(ni,nj):
                                return True
                return False

            for j in range(m):
                if grid[0][j]==0 and not visited[0][j]:
                    if dfs(0,j):
                        return True
            return False


        l,h = 0, n*m
        ans = 0
        while l<=h:
            mid = (l+h)//2
            if can_cross(mid):
                ans = mid
                l=mid+1
            else:
                h=mid-1
        return ans