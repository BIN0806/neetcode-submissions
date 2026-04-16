class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, l, seen = 0, 0, set()
        for r in range(len(s)):
            if s[r] in seen:
                l = r
            else:
                seen.add(s[r])
            count = max(count, r-l)
        return count