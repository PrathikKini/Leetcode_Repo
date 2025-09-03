class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p:(-p[0],p[1]))
        ans, n = 0, len(points)
        for i in range(n-1):
            y, yi=1<<31, points[i][1]
            for j in range(i+1,n):
                yj = points[j][1]
                if y>yj>=yi:
                    ans+=1
                    y=yj
                    if yi==yj: break
        return ans