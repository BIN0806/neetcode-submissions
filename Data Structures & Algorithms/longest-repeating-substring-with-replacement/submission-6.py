class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        best, l = 0, 0 
        char_to_count = defaultdict(int)
        
        max_f = 0
        for r in range(len(s)):
            char_to_count[s[r]] +=  1
            max_f = max(max_f, char_to_count[s[r]])
            while l < r and ((r-l+1) - max_f > k):
                char_to_count[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best

