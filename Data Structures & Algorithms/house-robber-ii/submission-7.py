class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob_h(nums):
            rob1, rob2 = 0, 0
            for num in nums: rob1, rob2 = max(rob1, num + rob2), rob1
            return rob1
            
        return max(nums[0], rob_h(nums[:-1]), rob_h(nums[1:]))