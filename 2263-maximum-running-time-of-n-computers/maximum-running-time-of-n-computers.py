class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """

        def isvalid(x,n,batteries):
            running_time=0
            for minute in batteries:
                running_time += min(minute, x)
            computers = running_time/x
            return computers>=n
        
        start=1 #lower cap
        end = sum(batteries) // n #upper cap
        maxTime=1

        # binary search bcoz monotonicity , if the n computers run for t min then it can also run for t-1 min but not more than t min , thus there is a peak min

        while start<=end:
            mid= start + (end-start)//2

            if isvalid(mid, n , batteries):
                maxTime=mid
                start=mid+1
            else:
                end= mid-1
        return maxTime