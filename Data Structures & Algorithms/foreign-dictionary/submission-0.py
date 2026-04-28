class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = collections.defaultdict(set)
        
        def alien_compare(word1, word2):
            n1 = len(word1)
            n2 = len(word2)
            length = min(n1, n2)
            for i in range(length):
                if word1[i] != word2[i]:
                    adj_list[word1[i]].add(word2[i])
                    return 
            

        n_words = len(words)
        for i in range(n_words-1):
            alien_compare(words[i], words[i+1])

        # topo sort = reverse (postorder DFS)
        result = ""
        visit, path = set(), set() # dfs, cycle detection
        def dfs(node):
            nonlocal result
            if node in path: return False
            if node in visit: return True

            visit.add(node)

            path.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            path.remove(node)

            result += node
            return True

        snapshot = list(adj_list.keys())
        for c in snapshot:
            if not dfs(c):
                return ""
        return result[::-1]
