class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        n,m = len(strs), len(strs[0])

        def is_ordered(col1,col2):
            for row in range(n):
                if strs[row][col1]>strs[row][col2]:
                    return False
            return True

        dp= [1]*m
        max_kept_cols=0

        for i in range(m):
            for j in range(i):
                if is_ordered(j,i):
                    dp[i]=max(dp[i],dp[j]+1)
            max_kept_cols=max(max_kept_cols, dp[i])
        
        return m-max_kept_cols