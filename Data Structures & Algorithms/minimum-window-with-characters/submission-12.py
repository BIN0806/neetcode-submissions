class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict      
        nS, nT = len(s), len(t)
        if nT > nS or (nT == nS and Counter(s) != Counter(t)):
            return ""

        freq_t, freq_s = Counter(t), defaultdict(int)
        l, pos = 0, None

        have, need = 0, sum(freq_t.values())
        for r in range(nS):    
            if s[r] in freq_t and freq_s[s[r]] == freq_t[s[r]]:
                print("increased h:", r, s[r])
                have += 1            
            freq_s[s[r]] += 1
            print(s[l:r+1])
            print(have, need)
            while l <= r and have == need: 
                if pos == None or (pos and len(s[l:r+1]) <= len(pos)):
                    print("new pos:", s[l:r+1])
                    pos = s[l:r+1]
                if s[l] in freq_t and freq_s[s[l]] == freq_t[s[l]]:
                    have -= 1
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    freq_s.pop(s[l])
                l += 1   
        return "" if pos == None else pos
