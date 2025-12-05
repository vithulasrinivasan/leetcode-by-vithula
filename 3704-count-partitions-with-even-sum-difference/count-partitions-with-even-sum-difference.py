class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        partition_cnt=0
        left_sum , right_sum = 0 , sum(nums)
        for i in nums:
            left_sum += i
            right_sum -= i
            if (left_sum - right_sum) % 2 ==0:
                partition_cnt+=1
            
        return partition_cnt if partition_cnt == 0 else partition_cnt - 1