class Solution(object):
    def longestBalanced(self, nums):
        n = len(nums)
        length = 0

        for i in range(n):
            odd = set()
            even = set()

            for j in range(i,n):

                if nums[j]%2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])

                if len(odd)==len(even):
                    length = max(length,j-i+1)
        return length