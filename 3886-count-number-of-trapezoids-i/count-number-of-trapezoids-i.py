from typing import List
from collections import Counter

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # Count how many points lie on each horizontal line (same y-coordinate)
        y_counts = Counter(y for x, y in points)
        
        # For each y-level, compute how many segments we can make: C(v, 2)
        choose = []
        for v in y_counts.values():
            if v >= 2:                      # need at least 2 points to form a segment
                choose.append(v * (v - 1) // 2)
        
        # If < 2 levels have segments, no trapezoids can be formed
        if len(choose) < 2:
            return 0
        
        # Count number of trapezoids: sum over all i < j of choose[i] * choose[j]
        ans = 0
        prefix_sum = 0
        for c in choose:
            ans += prefix_sum * c   # pairs with all previous levels
            prefix_sum += c
        
        return ans % (10**9 + 7)
