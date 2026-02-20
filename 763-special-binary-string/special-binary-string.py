class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        '''
        Solution : RECURSION + GREEDY
        1.divide into blocks
        2.make each block lexicographically best - recursive
        3.concatenate them reverse sorted block - greedy
        4.return the concatenate string
        '''
        count , i , res = 0, 0, []

        for j in range(len(s)):
            count+= 1 if s[j]=='1' else -1
            if count==0: #balanced
                res.append('1'+self.makeLargestSpecial(s[i+1:j])+'0') #recursively maximize the inner part and wrap it with 1 & 0
                i=j+1 #move to the next chunk

        res.sort(reverse=True)
        return ''.join(res)