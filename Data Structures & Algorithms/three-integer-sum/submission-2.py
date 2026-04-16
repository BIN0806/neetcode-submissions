class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, n = [], len(nums) 
        nums.sort()
        if n < 3:
            return result
        # [-1,0,1,2,-1,-4]
        # [-4, -1, -1, 0, 1, 2]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:                    
                if -(nums[j] + nums[k]) == nums[i]:
                    result.append([nums[j], nums[k], nums[i]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    k = n - 1
                elif -(nums[j] + nums[k]) < nums[i]:
                    k -= 1
                else:
                    j += 1
        return result