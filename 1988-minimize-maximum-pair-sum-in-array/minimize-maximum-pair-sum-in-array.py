class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair=0
        for i in range(len(nums)//2):
            pair=max(pair, nums[i] + nums[-1-i])
        return pair