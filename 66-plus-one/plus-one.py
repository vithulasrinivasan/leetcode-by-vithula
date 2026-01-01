class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[str(i) for i in digits]
        given=int("".join(digits))
        res=[]
        for i in str(given+1):
            res.append(int(i))
        return res

            