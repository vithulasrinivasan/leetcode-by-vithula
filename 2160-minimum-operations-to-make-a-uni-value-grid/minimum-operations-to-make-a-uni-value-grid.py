class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums=[]
        for row in grid:
            for num in row:
                nums.append(num)
        mod= nums[0] % x
        for num in nums:
            if num % x != mod:
                return -1
        nums.sort()
        median = nums[len(nums)//2]
        ops=0
        for num in nums:
            ops+= abs(num- median) // x
        return ops
