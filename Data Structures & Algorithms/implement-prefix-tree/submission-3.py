class TrieNode:
    def __init__(self):
        # from collections import defaultdict
        self.children = {}
        self.finish = False

class PrefixTree:
    def __init__(self):
        self.node = TrieNode()
        
    def insert(self, word: str) -> None:
        ptr = self.node
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.finish = True

    def search(self, word: str) -> bool:
        ptr = self.node
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.finish

    def startsWith(self, prefix: str) -> bool:
        ptr = self.node
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
    

