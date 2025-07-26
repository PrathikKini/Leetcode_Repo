class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_val = 0
        curr_val = 0
        for num in gain:
            curr_val+=num
            max_val = max(curr_val,max_val)
        return max_val