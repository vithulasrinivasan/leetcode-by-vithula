class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        mn = int(-1e14)
        dp = [[[mn] * 3 for _ in range(k + 1)] for _ in range(n + 1)]

        def f(i: int, k_left: int, state: int) -> int:
            if i == n:
                return 0 if state == 0 else mn
            if dp[i][k_left][state] != mn:
                return dp[i][k_left][state]

            p = prices[i]
            profit = mn

            # 1) do nothing
            profit = max(profit, f(i + 1, k_left, state))

            if state == 0:
                # Try buying or selling (to start a new transaction)
                profit = max(profit, f(i + 1, k_left, 1) - p)
                profit = max(profit, f(i + 1, k_left, 2) + p)
            elif k_left > 0:
                if state == 1:
                    # Complete buy-sell
                    profit = max(profit, f(i + 1, k_left - 1, 0) + p)
                else:
                    # Complete sell-buy
                    profit = max(profit, f(i + 1, k_left - 1, 0) - p)

            dp[i][k_left][state] = profit
            return profit

        return f(0, k, 0)

# from functools import lru_cache
# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         '''
#         ON A SINGLE DAY:-
#         1.buy a stock
#         2.short sell a stock
#         3.sell a bought stock
#         4.buy a short sell stock
#         5.skip

#         constraints:-
#         1.finish a transaction before starting a new one
#         2.either buy or short sell
#         3.cannot buy and sell on the same day
#         '''

#         n=len(prices)

#         @lru_cache(None)
#         def dfs(i,j,state):
#             # i-> current day
#             # j-> no of transactions used so far
#             # state -> 0,1,2
#             # state 0 - no transactions held
#             # state 1 - holding stock ie i have bought a stock already
#             # state 2 - holding short sell ie i have to buy a short sell stock 

#             if j>k:
#                 return float('-inf')
#             if i==n:
#                 return 0 if state==0 else float('-inf')
#             price = prices[i]

#             res=dfs(i+1,j,state) # do nothing 

#             if state==0: # nothing held

#                 res=max(res,dfs(i+1,j+1,1)-price) #buy
#                 res=max(res,dfs(i+1,j+1,2)+price) #short sell

#             elif state==1: # bought a stock already , shuld sell now

#                 res=max(res,dfs(i+1,j,0)+price) #sell

#             else: #state==2 already hv a short sell so buy it now
#                 res=max(res,dfs(i+1,j,0)-price) #buy a short sell

#             return res
        
#         return dfs(0,0,0)