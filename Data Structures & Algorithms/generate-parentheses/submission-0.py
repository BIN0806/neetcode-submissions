class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(cur_string, num_open, num_closed): 

            if num_open == num_closed == n:
                result.append(cur_string)
                return 

            if num_open < n:
                backtrack(cur_string + "(", num_open + 1, num_closed)
            if num_closed < n and num_open > num_closed:
                backtrack(cur_string + ")", num_open, num_closed + 1)

            # if num_open == n:

            # if num_closed == n: shouldn't happen
        backtrack("", 0, 0)
        return result 