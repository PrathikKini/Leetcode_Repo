class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [words[i] for i in range(0,len(words)) if i == 0 or sorted(words[i]) != sorted(words[i-1])]