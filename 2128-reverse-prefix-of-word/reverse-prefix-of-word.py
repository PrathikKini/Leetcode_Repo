class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            indexVal = word.index(ch)
            return word[:indexVal+1][::-1]+word[indexVal+1:]
        return word
        