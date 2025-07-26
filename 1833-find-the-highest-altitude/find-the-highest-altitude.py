class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        curr_val = 0
        for num in gain:
            curr_val+=num
            res.append(curr_val)
        return max(res)