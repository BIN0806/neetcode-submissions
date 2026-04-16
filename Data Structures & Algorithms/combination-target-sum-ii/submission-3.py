class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(idx, cur, total):
            if total == target:
                result.append(cur)
                return 
            if idx == len(candidates) or total > target:
                return 

            backtrack(idx + 1, cur + [candidates[idx]], total + candidates[idx])
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(idx+1, cur, total)

        backtrack(0, [], 0)
        return result