class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindrome = [word for word in words if word[::-1] == word]
        if palindrome:
            return palindrome[0]
        return ""