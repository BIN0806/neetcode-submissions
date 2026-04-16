class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, n = [], len(nums)
        if n < 3:
            return result
        # [-1, 0, 2, 2] 
        # [-2, -1, 0, 0, 2, 10]
        # [-1, 0, 1]
        # [-1, 0, 0, 1]
        # [-100, -1, 0, 1] 
        #  [-100, -2, 0, 0, 2]
        for i in range(n):
            target = nums[i]
            j = i + 1
            k = n - 1
            while j < k:                    
                if -(nums[j] + nums[k]) == target:
                    result.append([nums[j], nums[k], complements[nums[j]+ nums[k]]])
                elif -(nums[j] + nums[k]) < target:
                    j += 1
                else: 
                    k -= 1
        return result