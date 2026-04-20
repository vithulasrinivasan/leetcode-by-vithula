class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        dist=0
        for i in range(n):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    dist = max(dist, j-i)
        return dist
