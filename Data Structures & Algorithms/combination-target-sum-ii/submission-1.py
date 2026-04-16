class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(idx, cur, total):
            if idx == len(candidates) or total > target:
                return 
            if total == target:
                result.append(cur)
                return 
            print("Total: ", total + candidates[idx], "running_sum: ", cur + [candidates[idx]])
            backtrack(idx, cur + [candidates[idx]], total + candidates[idx])
            backtrack(idx+1, cur, total)
        backtrack(0, [], 0)
        return result