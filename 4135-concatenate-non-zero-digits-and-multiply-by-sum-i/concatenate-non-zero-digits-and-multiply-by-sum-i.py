class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return n
        n = str(n).replace("0","")
        return int(n) * sum(int(d) for d in n)
        