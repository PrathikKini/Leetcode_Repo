class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        sorted_vowels = sorted(ch for ch in s if ch in vowels)
        it = iter(sorted_vowels)
        result = []
        for ch in s:
            if ch in vowels:
                result.append(next(it))
            else:
                result.append(ch)
        return "".join(result)