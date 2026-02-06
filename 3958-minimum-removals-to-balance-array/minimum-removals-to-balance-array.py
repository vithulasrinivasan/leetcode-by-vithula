class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        a = 0
        for c in nums:
            a += c > nums[a] * k
        return a
        # nums.sort()
        # i=0
        # count = 0

        # for j in range(len(nums)):
        #     while nums[j] > nums[i] * k:
        #         i+=1

            
        #     count = max(count, j-i+1)
    
        # return len(nums) - count
