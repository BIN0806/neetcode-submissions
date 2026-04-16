class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def validate_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        result = []
        partition = []
        n = len(s)
        def dfs(i):
            if i >= n:
                result.append(partition.copy()) 
                return

            for j in range(i, n):
                if validate_palindrome(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j+1)
                    partition.pop()

        dfs(0)
        return result