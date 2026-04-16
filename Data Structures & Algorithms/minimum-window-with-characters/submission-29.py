class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict      
        nS, nT = len(s), len(t)
        if nT > nS or nT == 0:
            return ""

        freq_t, freq_s = Counter(t), defaultdict(int)
        l, pos = 0, None
        have, need = 0, nT

        for r in range(nS):    
            freq_s[s[r]] += 1

            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                have += 1 

            print(freq_s)
            if have == need and (pos == None or (pos and r-l+1 <= len(pos))):
                print("new pos:", s[l:r+1])
                pos = s[l:r+1]

            while l <= r and have == need:
                if have == need and (pos == None or (pos and r-l+1 <= len(pos))):
                    print("new pos:", s[l:r+1])
                    pos = s[l:r+1]
                    
                if freq_s[s[l]] <= freq_t[s[l]]:
                    have -= 1
                freq_s[s[l]] -= 1
                print(s[l], freq_s[s[l]])
                l += 1
            print(l, r)
        return "" if pos == None else pos
