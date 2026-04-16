class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n): # (0, .... n-1)
            if s[i] != s[n-1-i]:
                return False
        return True