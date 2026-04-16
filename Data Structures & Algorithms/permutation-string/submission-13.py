class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq substring window TP
        from collections import defaultdict

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        freq, l = defaultdict(int), 0
        match = Counter(s1)

        print(match)
        print(s1, n1, s2, n2)
        for r in range(n2):
            if (r-l+1) == len(s1):
                for char in s1:
                    if (freq[char] != match[char]):
                        break
                    return True
            print(freq)
            freq[s2[r]] += 1
            


            if (r-l+1) > len(s1):
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    freq.pop(s2[l])
                l += 1

        return False
        