class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0 # total sum of all the +ve numbers in the nums

        small_one , small_two = float("inf"), float("inf")
        # one can either be a smallest number n with rem of 1 or min sub sum of 2 nos: n1 and n2 with rem of 1
        # two can either be a smallest number n with rem of 2 or min sub sum of 2 nos: n1 and n2 with rem of 2
        
        for n in nums:
            total += n

            if n % 3 == 1:
                small_two = min (small_two , small_one + n) #notice the order bcoz the small_two depends on the prev small_one not the new updated one 

                # 4%3 = 1, 7%3=1 , 4+7 = 11, 11%3 = 2 => logic
                small_one = min(small_one , n)
            
            if n % 3 == 2:
                small_one = min (small_one , small_two + n)

                # 2+2 = 4, 4%3 = 1

                small_two = min(small_two , n)

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - small_one
        if total % 3 == 2:
            return total - small_two
