class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        char_set = set()
        for ch in s:
            if ch in char_set:
                char_set.remove(ch)
                length += 2
            else:
                char_set.add(ch)

        if char_set:
            length+=1
        return length