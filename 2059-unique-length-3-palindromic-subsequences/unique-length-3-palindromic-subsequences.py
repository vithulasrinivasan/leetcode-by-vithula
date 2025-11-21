class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters=set(s)
        count=0
        for l in letters:
            i , j =s.index(l) , s.rindex(l)
            between=set()
            for k in range(i+1 , j):
                between.add(s[k])
            count+=len(between)
        return count    