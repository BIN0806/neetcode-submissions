class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l, r):
            count = 0
            while 0 <= l and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
                count += 1
            return count 

        total = 0
        for i in range(n):
            total += expand(i, i) # center-wise (odd)
            total += expand(i, i + 1) # pair-wise (even)
        return total