class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count, n = Counter(nums), len(nums)
        freq = [[] for _ in range(n + 1)]

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(n, 0, -1): # Counting backwards on freq
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
