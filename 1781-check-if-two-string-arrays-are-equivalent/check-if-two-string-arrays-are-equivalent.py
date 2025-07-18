class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concat_word1 = ""
        concat_word2 = ""
        for word in word1:
            concat_word1+=word
        for word in word2:
            concat_word2+=word
        return concat_word1 == concat_word2