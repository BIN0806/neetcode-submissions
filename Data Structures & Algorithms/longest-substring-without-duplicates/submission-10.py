class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, l, seen = 0, 0, set()
        for r in range(len(s)):
            if s[r] in seen:
                count = max(count, r-l)
                l = r
            seen.add(s[r])
        if not count:
            return len(seen)
        return count