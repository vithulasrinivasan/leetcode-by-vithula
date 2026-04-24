class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        wildcards = moves.count('_')

        return max(abs ((l+wildcards) - r),

        abs(l - (r+wildcards)))
        