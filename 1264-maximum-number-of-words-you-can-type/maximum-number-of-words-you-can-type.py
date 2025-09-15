class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(not set(brokenLetters) & set(w) for w in text.split())