class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare_dict(dic_s, dic_t):
            for char in dic_t:
                if dic_s[char] < dic_t[char]:
                    return False
            return True 

        from collections import defaultdict
        nS, nT = len(s), len(t)
        if nT > nS:
            return ""

        freq_t = Counter(t)
        freq_s = defaultdict(int)

        l = 0
        possible = []
        for r in range(nS):
            if freq_s == freq_t:
                possible.append(s[l:r])
            freq_s[s[r]] += 1
            while l < r and compare_dict(freq_s, freq_t): 
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    freq_s.pop(s[l])
                l += 1   
                freq_s[s[l]] += 1
                print(freq_s)

        return min(possible, key=len)
