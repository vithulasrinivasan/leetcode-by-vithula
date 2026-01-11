class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 1. largest area of rectangle in the histogram - LRA
        # 2. prefix sum - precompute the bar heights

        def LRA(heights):
            n=len(heights)
            st=[]
            largestarea=0 # to store largest area
            area=0 #to store current area
            nse,pse=0,0 #to store the indices of next and prev smaller elements
            for i in range(n):
                while st and heights[st[-1]]>=heights[i]:
                    ind=st.pop()
                    pse=st[-1] if st else -1
                    nse=i
                    area=heights[ind] * (nse-pse-1)
                    largestarea=max(largestarea,area)
                st.append(i)
            while st:
                nse=n
                ind=st.pop()
                pse=st[-1] if st else -1
                area=heights[ind]*(nse-pse-1)
                largestarea=max(largestarea,area)
            return largestarea

        n,m = len(matrix),len(matrix[0])
        prefixsum=[[0]*m for _ in range(n)]
        for j in range(m):
            sum=0
            for i in range(n):
                sum+= int(matrix[i][j])
                if matrix[i][j]=='0':
                    prefixsum[i][j]=0
                    sum=0
                else:
                    prefixsum[i][j]=sum
        maxarea=0
        for i in range(n):
            area=LRA(prefixsum[i])
            maxarea=max(area,maxarea)
        return maxarea