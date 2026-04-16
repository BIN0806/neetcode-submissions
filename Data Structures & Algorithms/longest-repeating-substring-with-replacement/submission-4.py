class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        best, l = 0, 0 
        char_to_count = defaultdict(int)
        
        for r in range(len(s)):
            char_to_count[s[r]] +=  1
            while l < r and (((r-l+1) - max(char_to_count.values())) > k):
                char_to_count[l] -= 1
                l += 1
            best = max(best, r-l+1)
            if best == 5:
                print(l, r)
        return best

