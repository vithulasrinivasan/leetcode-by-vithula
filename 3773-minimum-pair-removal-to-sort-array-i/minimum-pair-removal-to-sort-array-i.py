class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count=0
        while len(nums)>1:
            isasc = True
            minsum=float("inf")
            targetindex=-1

            for i in range(len(nums)-1):
                pair_sum = nums[i]+nums[i+1]

                if nums[i]>nums[i+1]:
                    isasc=False

                if pair_sum<minsum:
                    minsum=pair_sum
                    targetindex=i

            if isasc:
                break
            
            count+=1
            nums[targetindex]=minsum
            nums.pop(targetindex+1)

        return count
                