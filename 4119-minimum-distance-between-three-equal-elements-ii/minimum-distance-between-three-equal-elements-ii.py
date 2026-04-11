class Solution:
    def minimumDistance(self, nums: List[int]) -> int:

        min_length = len(nums) + 1
        last_ind = [-1] * min_length
        second_to_last_ind = [-1] * min_length

        min_dist = math.inf

        for i, num in enumerate(nums):
            if second_to_last_ind[num] != -1:
                dist = i - second_to_last_ind[num]
                if min_dist > dist:
                    min_dist = dist
            second_to_last_ind[num] , last_ind[num] = last_ind[num], i

        if min_dist == math.inf:
            return -1
        return 2 * min_dist


        '''
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
        
        '''
