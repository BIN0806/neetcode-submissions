class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while not (l == r):
            while not s[r].isalnum():
                if (r < 0) or (l >= n):
                    return False
                r -= 1
            while not s[l].isalnum():
                if (r < 0) or (l >= n):
                    return False
                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True