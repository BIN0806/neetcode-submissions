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

    def search(self, word: str, ptr=None) -> bool:
        if not ptr:
            ptr = self.root
        for i in range(len(word)):
            if word[i] == ".":
                return any([self.search(word[i+1:], child) for child in ptr.children.values()])
            if word[i] not in ptr.children:
                return False
            ptr = ptr.children[word[i]]
        return True
       
