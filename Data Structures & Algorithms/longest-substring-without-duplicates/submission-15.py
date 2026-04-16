class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, l, seen = 0, 0, set()
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            else:
                seen.add(s[r])
            count = max(count, r-l+1)
        return count