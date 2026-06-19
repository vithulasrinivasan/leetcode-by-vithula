class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        ht=0
        for i in gain:
            ht+=i
            alt = max(alt , ht)

        return alt 