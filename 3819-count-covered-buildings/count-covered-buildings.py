class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n+1)
        max_col = [0] * (n+1)

        min_row = [n+1] * (n+1)
        min_col = [n+1] * (n+1)

        for [x,y] in buildings: # for each row and col , find both the extreme coordinates
            max_col[x] = max(max_col[x],y)
            min_col[x] = min(min_col[x], y)

            max_row[y] = max(max_row[y],x)
            min_row[y] = min(min_row[y],x)
        
        covered=0
        for [x,y] in buildings:
            if (x < max_row[y] and x> min_row[y] and y<max_col[x] and y>min_col[x]):
                covered+=1

        return covered
