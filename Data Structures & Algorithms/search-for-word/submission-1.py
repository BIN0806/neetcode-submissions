class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        str_len = len(word)
        rows, cols = len(board), len(board[0])
        DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        seen = set()

        def out_of_bounds(r, c):
            return r >= rows or c >= cols or r < 0 or c < 0 

        def dfs(r, c, i):
            # print(cur_string)
            if i == str_len:
                return True
            if out_of_bounds(r, c) or (r,c) in seen or word[i] != board[r][c]:
                return False

            seen.add((r, c))
            res = False
            for dx, dy in DIR:
                res = res or dfs(r + dx, c + dy, i + 1)
            seen.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False

