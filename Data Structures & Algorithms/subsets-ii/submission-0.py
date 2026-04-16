class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(arr, idx):
            if idx == len(nums):
                res.append(arr)
                return
        
            backtrack(arr + [nums[idx]], idx+1)

            # Skip 
            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1
            backtrack(arr, idx+1)
        
        backtrack([], 0)
        return res