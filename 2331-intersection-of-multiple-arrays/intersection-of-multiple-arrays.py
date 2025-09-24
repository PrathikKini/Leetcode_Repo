class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        flat_lst = [x for lst in nums for x in lst]
        cntr = Counter(flat_lst)
        items = cntr.items()
        return sorted([k for (k,v) in items if v == len(nums)])