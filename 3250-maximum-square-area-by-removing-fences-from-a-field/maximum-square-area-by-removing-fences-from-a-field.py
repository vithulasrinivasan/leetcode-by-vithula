class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        MOD = 10**9 + 7

        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])

        def get_gaps(arr):
            gaps = set()
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    gaps.add(arr[j] - arr[i])
            return gaps

        h_gaps = get_gaps(h)
        v_gaps = get_gaps(v)

        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
