import math
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7

        n=len(complexity)
        for i in range(1,n):
            if complexity[i]<=complexity[0]:
                return 0

        return math.factorial(n-1) % mod