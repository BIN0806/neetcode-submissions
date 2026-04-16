class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(cur_sum, numbers ,idx):
            if idx == len(nums):
                return 
            if cur_sum > target:
                return 
            if cur_sum == target:
                result.append(numbers)
                return

            backtrack(cur_sum + nums[idx], numbers + [nums[idx]], idx)
            backtrack(cur_sum, numbers, idx + 1)

        backtrack(0, [], 0)
        return result