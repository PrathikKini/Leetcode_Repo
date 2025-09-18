class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_set = set(list1) & set(list2)
        index_sum = {}
        for i, r in enumerate(list1):
            if r in common_set:
                index_sum[r] = i

        for i, r in enumerate(list2):
            if r in common_set:
                index_sum[r] += i

        min_val = min(index_sum.values())
        return [r for r, s in index_sum.items() if s == min_val]