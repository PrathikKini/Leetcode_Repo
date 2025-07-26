class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s) // 2
        vowels = set('aeiou')
        cnt1 = sum(1 for ch in s[:n] if ch in vowels)
        cnt2 = sum(1 for ch in s[n:] if ch in vowels)
        return cnt1 == cnt2