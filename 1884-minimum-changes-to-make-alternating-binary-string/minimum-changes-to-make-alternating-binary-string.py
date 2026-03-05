class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        s=list(s)
        cnt=0
        for i in range(1,n):
            if s[i]==s[i-1]:
                if s[i]=='0':
                    s[i]='1'
                else:
                    s[i]='0'
                cnt+=1
            
        return min(cnt, n-cnt)
        