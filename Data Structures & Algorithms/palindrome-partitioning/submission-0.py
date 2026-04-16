class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def validate_palindrome(s):
            return s == s[::-1]

        result = []
        n = len(s)
        def backtrack(cur_list, i):
            if i >= n:
                result.append(cur_list) 
                return

            for j in range(i, n):
                if validate_palindrome(s[i:j+1]):
                    backtrack(cur_list + [s[i:j+1]], j+1)

        backtrack([], 0)
        return result