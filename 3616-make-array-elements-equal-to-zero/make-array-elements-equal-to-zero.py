class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        t, l, c = sum(nums), 0, 0
        for i in range(len(nums)):
            rs = t - l - nums[i]
            if nums[i] == 0:
                if l == rs:
                    c+=2
                elif l == rs - 1 or l - 1 == rs:
                    c+=1
            l += nums[i]
        return c