class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        def dfs(s: str) -> str:
            if s not in seen:
                seen.add(s)
                addA = list(s)
                for i, c in enumerate(addA):
                    if i % 2 == 1:
                        addA[i] = str((int(c) + a) % 10)
                return min(s, dfs(''.join(addA)), dfs(s[b :] + s[: b]))
            return s    
                
        seen = set()
        return dfs(s)