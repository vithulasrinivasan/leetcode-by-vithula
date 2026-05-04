class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        res=[]
        n=len(matrix)
        for i in range(n):
            curr=[]
            for j in range(n-1,-1,-1):
                curr.append(matrix[j][i])
            res.append(curr)
            
        for i in range(n):
            for j in range(n):
                matrix[i][j]=res[i][j]