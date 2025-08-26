class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        pairs = max(dimensions, key=lambda x : (x[0]**2+x[1]**2,x[0]+x[1]))
        return pairs[0] * pairs[1]