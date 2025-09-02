class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (-p[0],p[1]))
        n, ans = len(points), 0
        for i in range(n-1):
            y = 1<<31
            for j in range(i+1,n):
                if y > points[j][1] >= points[i][1]:
                    ans+=1
                    y = points[j][1]
        return ans