class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, l, seen = 0, 0, set()
        for r in range(len(s)):
            if not s[r] in seen and r == len(s)-1:
                count = max(count, r-l+1)
            if s[r] in seen:
                count = max(count, r-l)
                while s[l] != s[r]:
                    l += 1
                l += 1
            else:
                seen.add(s[r])
        return count