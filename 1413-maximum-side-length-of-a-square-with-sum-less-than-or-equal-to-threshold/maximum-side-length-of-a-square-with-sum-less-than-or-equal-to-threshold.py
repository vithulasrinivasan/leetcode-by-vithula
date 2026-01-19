class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n = len(mat), len(mat[0])
        
        # 2D prefix sum grid
        
        p =[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(n+1):
                p[i][j] = p[i-1][j]+p[i][j-1]-p[i-1][j-1]+mat[i-1][j-1]

        def summ(x1,y1,x2,y2):
            return p[x2][y2] - p[x1-1][y2] - p[x2][y1-1] + p[x1-1][y1-1]

        ans=0
        side=min(m,n) # max side length

        # (i,j) -> top left corner of the square
        # c -> possible side length

        for i in range(1,m+1): 
            for j in range(1,n+1):
                for c in range(ans+1,side+1):
                    if(
                        i+c-1 <= m and j+c-1<=n and 
                        summ(i,j,i+c-1, j+c-1) <= threshold
                    ):
                        ans+=1
                    else:
                        break

        return ans