class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(subset, i):
            if i == len(nums): 
                result.append(subset)
                return 

            backtrack(subset + [nums[i]], i + 1)
            backtrack(subset, i + 1)
                 
        backtrack([], 0)
        return result