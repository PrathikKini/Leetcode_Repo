class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        p_land = set()
        a_land = set()
        R, C = len(heights), len(heights[0])
        def spread(i, j, land):
            land.add((i,j))
            for x,y in ((i+1,j), (i, j+1), (i-1,j), (i,j-1)):
                if (0<=x<R and 0<=y<C and heights[x][y] >= heights[i][j]
                and (x,y) not in land):
                    spread(x, y, land)

        for i in range(R):
            spread(i, 0, p_land)
            spread(i, C-1, a_land)
        for j in range(C):
            spread(0, j, p_land)
            spread(R-1, j, a_land)
        return list(p_land & a_land)