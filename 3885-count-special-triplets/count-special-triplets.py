class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        num_cnt ={} # tot occurences of each num in nums - precomputed
        num_partial_cnt ={} # tot occurences of each num in nums upto current traversal position
        # while enumerating 

        for num in nums:
            num_cnt[num] = num_cnt.get(num,0)+1
        
        ans=0

        for num in nums:
            target = num*2
            l_cnt = num_partial_cnt.get(target,0)

            num_partial_cnt[num]=num_partial_cnt.get(num,0)+1

            r_cnt= num_cnt.get(target,0) - num_partial_cnt.get(target,0)

            ans += (l_cnt * r_cnt) 

        return ans % (10**9 + 7)