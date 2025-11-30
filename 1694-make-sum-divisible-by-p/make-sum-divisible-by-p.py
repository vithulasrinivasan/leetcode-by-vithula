class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total=sum(nums)
        rem=total%p
        if rem==0:
            return 0
        res=len(nums)
        cur=0
        d={0:-1}
        for i,n in enumerate(nums):
            cur=(cur+n)%p
            prefix=(cur-rem+p)%p

            if prefix in d:
                l=i-d[prefix]
                res=min(res,l)
            d[cur]=i

        return -1 if res==len(nums) else res