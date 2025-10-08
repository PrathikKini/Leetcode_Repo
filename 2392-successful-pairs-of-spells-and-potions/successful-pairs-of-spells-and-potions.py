class Solution:
    def validpos(self, potions: List[int], success: int,  spell: int) -> List[int]:
        potion_needed = (success + spell - 1) // spell
        l, r = 0, len(potions)
        while l < r:
            m = l + (r-l) // 2
            if potions[m] >= potion_needed:
                r = m
            else:
                l = m + 1
        return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            res.append(len(potions)-self.validpos(potions,success,spell))
        return res