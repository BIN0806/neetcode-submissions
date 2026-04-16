class TrieNode:
    def __init__(self, char, finish):
        # from collections import defaultdict
        self.children = {}
        self.char = char
        self.finish = finish

class PrefixTree:
    def __init__(self):
        self.node = TrieNode('-1', False)
        
    def insert(self, word: str) -> None:
        ptr = self.node
        for i in range(len(word)):
            if word[i] not in ptr.children:
                ptr.children[word[i]] = TrieNode(word[i], False)
            ptr = ptr.children[word[i]]
            if i == len(word) - 1:
                ptr.finish = True
        
    def search(self, word: str) -> bool:
        ptr = self.node
        for i in range(len(word)):
            if word[i] not in ptr.children:
                return False
            ptr = ptr.children[word[i]]
        return ptr.finish

    def startsWith(self, prefix: str) -> bool:
        ptr = self.node
        for i in range(len(prefix)):
            if prefix[i] not in ptr.children:
                return False
            ptr = ptr.children[prefix[i]]
        return len(ptr.children) != 0 or ptr.finish
    

