class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])

        inf = 10**20

        ans  = [[inf]*(c-k+1) for _ in range(r-k+1)]

        for dr in range(r-k+1):
            for dy in range(c-k+1):

                v = set()

                for x in range(k):
                    for y in range(k):
                        v.add(grid[dr+x][dy+y])

                r = list(sorted(v))

                for a,b in zip(r, r[1:]):
                    ans[dr][dy] = min(ans[dr][dy], b-a)

                if ans[dr][dy] == inf:
                    ans[dr][dy] = 0

        return ans
