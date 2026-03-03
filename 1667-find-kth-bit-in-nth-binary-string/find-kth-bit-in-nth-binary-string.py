class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        invert=0
        length=(1<<n)-1
        while k > 1:
            if k == length // 2 + 1:
                return '1' if invert % 2 == 0 else '0'
            elif k > length // 2 + 1:
                k = length - k + 1
                invert += 1
            length //= 2
        
        return '0' if invert % 2 == 0 else '1'