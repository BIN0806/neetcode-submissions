class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while 0 <= l and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l+1:r]
        strings = []
        for i in range(n):
            strings.append(expand(i, i))
            strings.append(expand(i, i + 1))
        return max(strings, key=len)
