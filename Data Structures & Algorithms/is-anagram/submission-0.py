class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import counter
        return collections.counter(s) == collections.counter(t) 