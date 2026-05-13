class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2*limit + 2)

        for i in range(n//2):
            a = min(nums[i], nums[n-i-1])
            b = max(nums[i], nums[n-i-1])

            diff[2] += 2
            diff[a+1] -= 1
            diff[a+b] -= 1
            diff[a+b+1] += 1
            diff[b+limit+1] += 1

        ops=n
        current = 0

        for target in range(2, 2*limit +1):
            current += diff[target]
            if current < ops:
                ops = current

        return ops

