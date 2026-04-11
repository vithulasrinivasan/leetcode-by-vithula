class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}
        
        for i, num in enumerate(nums):
            if num not in pos:
                pos[num] = []
            pos[num].append(i)
        
        ans = float('inf')

        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                distance = 2 * (indices[i + 2] - indices[i])
                ans = min(ans, distance)
        
        return -1 if ans == float('inf') else ans
        

