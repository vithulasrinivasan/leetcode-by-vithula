class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007
        x, y = 6, 6 
        
        # x -> Alternating - 1st & last col same 
        #  RYR, YRY, GRG, RGR, YGY, GYG 
        # y -> All different - all 3 col different 
        #  RGB, RGY, YRG, YGR, GRY, GYR

        for i in range(2,n+1):
            x1 = (3*x + 2*y) % mod
            y1 = (2*x + 2*y) % mod
            x,y = x1,y1
        return (x+y) % mod