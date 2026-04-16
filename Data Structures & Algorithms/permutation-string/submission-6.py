class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq substring window TP
        from collections import defaultdict

        n1, n2 = len(s1), len(s2)

        temp = s1
        s1 = s1 if n2 >= n1 else s2
        s2 = s2 if n2 >= n1 else temp

        temp = n1
        n1 = min(n1, n2)
        n2 = max(temp, n2)

        freq, l = defaultdict(int), 0
        match = Counter(s1)

        cur_key_count = 0
        print(match)
        for r in range(n2):
            print(freq)
            freq[s2[r]] += 1
            cur_key_count += 1

            if (freq == match):
                return True

            if (cur_key_count) >= len(s1):
                freq[s2[l]] -= 1
                if freq[s2[l]] == 0:
                    freq.pop(s2[l])
                cur_key_count -= 1
                l += 1

        return False
        