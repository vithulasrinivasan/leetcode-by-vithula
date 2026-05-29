class Solution:
    def minElement(self, nums: List[int]) -> int:

        def summ(n):

            ans=0

            while n>0:
                ans += n%10
                n //= 10

            return ans

        res= 37

        for i in nums:
            res= min(res,summ(i))

        return res