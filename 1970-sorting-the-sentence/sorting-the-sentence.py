class Solution:
    def sortSentence(self, s: str) -> str:
        nums = [int(word[-1]) for word in s.split()]
        words = [word[:-1] for word in s.split()]

        res = [''] * len(words)
        for i, word in enumerate(words):
            res[nums[i]-1] = word
        return " ".join(res)