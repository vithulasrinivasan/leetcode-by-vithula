class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k%2 == 0:
            return -1
        cur=1
        for i in range(1, k+1):
            if cur%k==0:
                return i
            cur = 10*(cur%k) + 1
        return -1
        
        