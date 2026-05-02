class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {} # char -> TrieNode 

    def insert(self, word):
        ptr = self 
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        DIR = [(0,1), (0, -1), (1, 0), (-1,0)]
        n_rows, n_cols = len(board), len(board[0])
        def traversable(r, c): return 0 <= r < n_rows and 0 <= c < n_cols and (r, c) not in visit 

        root = TrieNode()
        for word in words:
            root.insert(word)

        visit = set()
        result = set()

        def dfs(r, c, node, word):
            if not traversable(r, c):
                return 
            if board[r][c] not in node.children: 
                return

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.end:
                result.add(word)

            for dx, dy in DIR:
                dfs(r+dx, c+dy, node, word)

            visit.remove((r,c))

        for r in range(n_rows):
            for c in range(n_cols):
                dfs(r, c, root, "")

        return list(result)
