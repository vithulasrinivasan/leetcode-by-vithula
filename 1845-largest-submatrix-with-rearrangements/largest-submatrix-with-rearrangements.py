class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])

        largest = 0
        streak = [0] * c
        for x in range(r):
            for y in range(c):
                if matrix[x][y]==1:
                    streak[y]+=1
                else:
                    streak[y]=0
            
            cells = list(sorted(streak, reverse = True))

            for index, v in enumerate(cells,start=1):
                largest = max(largest , index*v)
                

        return largest

        '''

        10^18 -> o(1)
        10^8 -> o(n)
        10^5 -> o(n**2) or o(n logn)

        '''