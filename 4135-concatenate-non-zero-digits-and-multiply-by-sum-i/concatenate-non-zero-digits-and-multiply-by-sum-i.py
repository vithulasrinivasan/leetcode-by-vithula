class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """

        digits=[ch for ch in str(n) if ch !='0']
        x= int("".join(digits) if digits else 0)
        s=sum(int(d) for d in str(x))

        return s*x
        
        # if n == 0:
        #     return n
        # n = str(n).replace("0","")
        # return int(n) * sum(int(d) for d in n)
        