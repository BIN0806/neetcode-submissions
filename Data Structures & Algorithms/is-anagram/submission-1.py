class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return collections.Counter(s) == collections.Counter(t) 