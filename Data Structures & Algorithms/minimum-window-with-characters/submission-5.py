class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare_dict(dic_s, dic_t):
            for char in dic_t:
                if dic_s[char] < dic_t[char]:
                    return False
            return True 

        from collections import defaultdict
        nS, nT = len(s), len(t)
        if nT > nS or (nT == nS and Counter(s) == Counter(t)):
            return ""

        freq_t = Counter(t)
        freq_s = defaultdict(int)
        print("counter t", freq_t)
        l = 0
        pos = " " * len(s)
        for r in range(nS):                
            freq_s[s[r]] += 1
            print(l,r)
            while l <= r and compare_dict(freq_s, freq_t): 
                print("enter")
                if len(s[l:r]) <= len(pos):
                    pos = s[l:r+1]
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    freq_s.pop(s[l])
                l += 1   
                print(freq_s)
            print(len(s[l:r]))
        return pos
