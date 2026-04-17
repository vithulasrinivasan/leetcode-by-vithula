class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = defaultdict(list) # reverse
        ans = inf

        for i, num in enumerate(nums):
            if num in seen:
                ans = min(ans , i - seen[num])

            seen[int(str(num)[::-1])] = i

        return -1 if ans == inf else ans