class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        low, high , totalarea = float('inf'), float('-inf'), 0
        for x,y,l in squares:
            totalarea+= l*l
            low=min(low,y)
            high=max(high, y+l)

        targetarea= totalarea/2.0

        for i in range(60):
            mid=(low+high)/2.0
            currarea=0
            for _,y,l in squares:
                curry= max(0,min(l,mid-y)) #height below
                currarea+= l*curry

            if currarea<targetarea:
                low=mid
            else:
                high=mid
        
        return mid