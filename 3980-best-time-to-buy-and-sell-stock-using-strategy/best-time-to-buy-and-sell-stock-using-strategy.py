class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        profitsum = [0] * (n+1)
        pricesum = [0] * (n+1)

        for i in range(n):
            pricesum[i+1] = pricesum[i] + prices[i]
            profitsum[i+1] = profitsum[i] + prices[i] * strategy[i]

        res=profitsum[n]
        
        for i in range(k-1,n):
            leftprofit = profitsum[i-k+1]
            rightprofit = profitsum[n] - profitsum[i+1]
            changeprofit = pricesum[i+1] - pricesum[i-k//2+1]
            res=max(res, leftprofit+changeprofit+rightprofit)
        
        return res