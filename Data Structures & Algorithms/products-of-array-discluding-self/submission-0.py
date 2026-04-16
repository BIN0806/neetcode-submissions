class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [ 1 for i in range(len(nums))]
        # brute force is to do every index but i => O(n^2)
        total_product = 1
        for num in nums: 
            total_product *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = 0
                continue
            result[i] = int(total_product / nums[i])
        return result