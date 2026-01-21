class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]
        for n in nums:
            if n & 1:
                ans.append(n & ~(((n+1) & ~n)>>1))
            else:
                ans.append(-1)
        return ans
        
        
        ''' BRUTE FORCE:
        ans=[]
        for n in nums:
            found = False
            for i in range(1,n):
                if i | i+1 == n:
                    ans.append(i)                   
                    found=True
                    break
            if found == False:
                ans.append(-1)
        return ans
        '''    
