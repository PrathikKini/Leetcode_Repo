class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        res = []
        count = Counter(arr1)
        for num in arr2:
            res.extend([num] * count[num])
            count[num] = 0
        for num in sorted(count.elements()):
            res.append(num)
        return res