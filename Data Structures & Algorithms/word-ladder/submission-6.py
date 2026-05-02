class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: 
            return 0

        adj_list = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                wild_card_string = word[:i] + "*" + word[i+1:]
                adj_list[wild_card_string].append(word)
        # connection from all words, now run BFS starting at beginWord until endWord
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord: 
                    return res

                for j in range(len(word)):
                    wild_card_string = word[:j] + "*" + word[j+1:]
                    for nei in adj_list[wild_card_string]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)

            res += 1
        return 0