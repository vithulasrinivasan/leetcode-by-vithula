class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        i=0
        j=0
        max_dist=0

        while True:
            try:
                if nums1[i]<=nums2[j]:
                    max_dist=max(max_dist,j-i)
                    j+=1
                else:
                    i+=1
            except:
                break
        return max_dist

        # i, j = 0,0
        # dist = 0

        # while i< len(nums1) and j<len(nums2):
        #     if nums1[i] <= nums2[j]:
        #         dist = max(dist, j-i)
        #         j+=1
        #     else:
        #         i+=1
        #         if i>j:
        #             j=i
        
        # return dist

