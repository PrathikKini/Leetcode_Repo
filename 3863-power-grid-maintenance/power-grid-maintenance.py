class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        def find(u):
            while root[u] != u:
                root[u] = root[root[u]]
                u = root[u]
            return u

        root, online, grid = list(range(c + 1)), [1] * (c + 1), {}
        for u, v in connections:
            ru, rv = find(u), find(v)
            if ru < rv:
                root[rv] = ru
            elif ru > rv:
                root[ru] = rv

        for u in range(c, 0, -1):
            grid.setdefault(find(u), []).append(u)

        ret = []
        for op, u in queries:
            if op == 2:
                online[u] = 0
            elif online[u]:
                ret.append(u)
            else:
                pq = grid[find(u)]
                while pq and not online[pq[-1]]:
                    pq.pop()

                ret.append(pq[-1] if pq else -1)
        return ret