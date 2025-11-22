class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ops=0
        for i in nums:
           if i%3 !=0:
            ops+=1
        return ops

        #rem = i%3 
           # rem can be 0,1,2
           # if rem 0 , nthg to add
           # if rem 1 , subtract 1 
           # if rem 2 , add 1