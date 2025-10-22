class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)

        cnt = Counter()
        res = i = j = 0
        for a in nums:
            while j < n and nums[j] <= a + k:
                cnt[nums[j]] += 1
                j += 1
            while i < n and nums[i] < a - k:
                cnt[nums[i]] -= 1
                i += 1
            cur = min(j - i, cnt[a] + numOperations)
            res = max(res, cur)
        
        i = 0
        for j in range(n):
            while nums[i] + k + k < nums[j]:
                i+=1
            res = max(res, min(j - i + 1, numOperations))
        return res
