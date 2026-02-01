class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        summ = nums[0]
        nums[1:n] = sorted(nums[1:n])
        summ += nums[1] + nums[2]
        return summ
            