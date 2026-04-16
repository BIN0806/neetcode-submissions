class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            char = [0] * 26
            for c in string:
                char[ord(c)-ord('a')] += 1
            result[tuple(char)].append(string)

        return result.values()