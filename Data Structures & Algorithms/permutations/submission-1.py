class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def backtrack(lst, seen):
            if len(lst) == n:
                res.append(lst)
                return 

            for i in range(n):
                if nums[i] not in seen:
                    seen.add(nums[i])
                    backtrack(lst + [nums[i]], seen)
                    seen.remove(nums[i])
                    
        backtrack([], set())
        return res