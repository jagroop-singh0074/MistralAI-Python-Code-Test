class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while i < len(chars):
            count = 1
            while i + count < len(chars) and chars[i + count] == chars[i]:
                count += 1
            chars[j] = chars[i]
            j += 1
            if count > 1:
                for digit in str(count):
                    chars[j] = digit
                    j += 1
            i += count
        return j
