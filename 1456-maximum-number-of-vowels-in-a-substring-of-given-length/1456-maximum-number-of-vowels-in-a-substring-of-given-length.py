class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        ans = cnt
        left = 0
        for right in range(k, len(s)):
            if s[left] in vowels:
                cnt -= 1
            left += 1
            if s[right] in vowels:
                cnt += 1
            ans = max(ans, cnt)
        return ans

        