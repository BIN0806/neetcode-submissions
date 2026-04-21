class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def differ_by_one(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
            return diff == 1

        from collections import defaultdict
        edges = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if differ_by_one(wordList[j], wordList[i]):
                    edges[wordList[j]].append(wordList[i])
                    edges[wordList[i]].append(wordList[j])
            
        # self.min_path = float('inf')
        # visit = set()
        # def dfs(node, path):
        #     if path >= self.min_path:
        #         return 
        #     if node == endWord:
        #         self.min_path = min(self.min_path, path)
        #         return 
        #     visit.add(node)    
        #     for nei in edges[node]:
        #         if nei not in visit:
        #             dfs(nei, path + 1)
        #     visit.remove(node)    
        # dfs(beginWord, 1)

        # return self.min_path if self.min_path != float('inf') else 0

        from collections import deque
        queue = deque()
        queue.append((beginWord, 1))
        visit = set()
        self.min_path = float('inf')
        while queue:
            node, path_len= queue.popleft()

            if node == endWord:
                return path_len

            for nei in edges[node]:
                if nei not in visit:
                    queue.append((nei, path_len + 1))
                    visit.add(nei)

        return self.min_path if self.min_path != float('inf') else 0


