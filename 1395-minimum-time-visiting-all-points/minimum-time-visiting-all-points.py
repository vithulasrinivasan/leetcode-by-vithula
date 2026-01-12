class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        time=0
        for i in range(len(points)-1):
            curx , cury = points[i]
            nextx, nexty = points[i+1]
            time += max(abs(nextx-curx), abs(nexty-cury))
        return time

    '''
    Mathematical Proof
    Let dx = |x2 - x1| and dy = |y2 - y1|. We want to reach the destination in minimum steps. The optimal strategy is to move diagonally as much as possible.

    You can only move diagonally until one of the distances becomes 0. This means you can take min(dx,dy) diagonal steps.

    This reduces both dx and dy by min(dx, dy).

    Time taken so far: min(dx, dy).

    After these moves, the smaller distance becomes 0. The remaining distance for the larger dimension is max(dx, dy) - min(dx, dy).
    We cover this remaining distance with straight moves (horizontal or vertical).

    Time taken for this part: max(dx, dy) - min(dx, dy).

    Total = min(dx, dy) + max(dx, dy) - min(dx, dy) = max(dx,dy)
'''