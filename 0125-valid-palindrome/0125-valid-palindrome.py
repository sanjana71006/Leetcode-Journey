class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        for ch in s:
            if ch.isalnum():
                a += ch.lower()
        n = len(a)
        if n == 0:
            return True
        l, r = 0, n - 1
        while l < r:
            if a[l] != a[r]:
                return False
            l += 1
            r -= 1
        return True