class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        from collections import defaultdict, deque
        edges = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*"+ word[j+1:]
                edges[pattern].append(word) # why is it faster to add combinations of edges
            
        queue = deque([beginWord])
        visit = set([beginWord])
        res = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*"+ word[j+1:]
                    for neiWord in edges[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            queue.append(neiWord)
            res += 1
        return 0

