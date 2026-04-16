class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq substring window TP
        from collections import defaultdict

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        freq, l = defaultdict(int), 0
        match = Counter(s1)

        for r in range(n2):
            freq[s2[r]] += 1
            if (r-l+1) == len(s1) and freq == match:
                return True
        
            if (r-l+1) >= len(s1):
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    freq.pop(s2[l])
                l += 1

        return False
        