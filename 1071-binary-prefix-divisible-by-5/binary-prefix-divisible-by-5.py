class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """

        n=len(nums)
        ans=[]
        prefix=0
        for i in range(n):
            prefix += 2**(n-i) * nums[i]
            if prefix % 5 ==0:
                ans.append(True)
            else:
                ans.append(False)
        return ans