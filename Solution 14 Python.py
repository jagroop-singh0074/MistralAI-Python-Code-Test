class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        max_count = 0
        curr_count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                curr_count += 1
            if i >= k and s[i - k] in vowels:
                curr_count -= 1
            max_count = max(max_count, curr_count)
        return max_count
