class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(idx, cur, total):
            if total > target:
                return 
            if total == target:
                result.append(cur)

            backtrack(idx+1, cur+[candidates[idx]], total + candidates[idx])
            backtrack(idx+1, cur, total)

        return result