class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, n = 1, max(piles), len(piles)

        def can_lower(k): # counts # of hours to finish all bananas with k bananas per hour
            count = 0
            for p in piles:
                count += math.ceil(p / k)
            return count <= h

        piles.sort()
        while l <= r:
            m = (l + r) // 2
            print(l, r, m)
            if can_lower(m):
                r = m - 1
            else:
                l = m + 1
        return l

        # [1, 4, 3, 2]

        # [4, 10, 23, 25]
        # 