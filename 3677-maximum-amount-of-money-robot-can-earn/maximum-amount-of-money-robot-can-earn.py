class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        INF = 10 ** 20
        R = len(coins)
        C = len(coins[0])

        @cache
        def f(x, y, skips):
            if x == R - 1 and y == C - 1:
                if skips == 0:
                    return coins[x][y]
                return max(coins[x][y], 0)

            best = -INF
            if skips > 0:
                # we can skip this one
                # go right
                if y + 1 < C:
                    best = max(best, f(x, y + 1, skips - 1))
                if x + 1 < R:
                    best = max(best, f(x + 1, y, skips - 1))
            
            if y + 1 < C:
                best = max(best, f(x, y + 1, skips) + coins[x][y])
            if x + 1 < R:
                best = max(best, f(x + 1, y, skips) + coins[x][y])

            return best

        r = f(0, 0, 2)
        f.cache_clear()
        return r


            