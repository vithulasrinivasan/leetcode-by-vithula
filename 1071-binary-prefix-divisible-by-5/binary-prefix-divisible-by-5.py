class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """

        #shifting the digits left == multiplying it by 2
        # if it is divisible by 5 , reinitialize it to 0

        ans =[]
        curr =0
        for bit in nums:
            curr = (curr<<1) + bit
            ans.append(curr%5==0)
        return ans


        # brute force
        # n=len(nums)
        # ans=[]
        # prefix=0
        # for i in range(n):
        #     prefix += 2**(n-i) * nums[i]
        #     if prefix % 5 ==0:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        # return ans