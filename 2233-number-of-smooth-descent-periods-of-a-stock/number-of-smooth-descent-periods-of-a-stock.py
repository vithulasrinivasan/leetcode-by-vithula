class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descent = 1          
        streak = 1           
        
        for j in range(1, len(prices)):
            if prices[j] == prices[j-1] - 1:
                streak += 1
            else:
                streak = 1   
            
            descent += streak
        
        return descent
