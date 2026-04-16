class TrieNode:
    from collections import defaultdict
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(TrieNode)

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(j, ptr):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in ptr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in ptr.children:
                        return False
                    ptr = ptr.children[word[i]]
            return ptr.isWord
        return dfs(0, self.root)
       
