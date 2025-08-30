class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        count = Counter(tiles)
        def backtrack(counter):
            total = 0
            for ch in counter:
                if counter[ch]>0:
                    total+=1
                    counter[ch] -= 1
                    total+=backtrack(counter)
                    counter[ch] += 1
            return total
        return backtrack(count)

        