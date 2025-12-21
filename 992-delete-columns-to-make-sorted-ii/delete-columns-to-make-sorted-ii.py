class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n,m = len(strs), len(strs[0])
        sorted_pairs=[False]*(n-1)

        delete=0

        for col in range(m):
            flag=False
            for row in range(n-1):
                if not sorted_pairs[row] and strs[row][col]>strs[row+1][col]:
                    flag=True
                    break
            if flag:
                delete+=1
                continue

            for row in range(n-1):
                if not sorted_pairs[row] and strs[row][col]<strs[row+1][col]:
                    sorted_pairs[row]=True

        return delete