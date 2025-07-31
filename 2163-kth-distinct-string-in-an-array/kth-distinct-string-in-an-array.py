class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for num in arr:
            freq[num] = 1 + freq.get(num,0)
        unique = [key for key,val in freq.items() if val == 1]
        return "" if len(unique) < k else unique[k-1]