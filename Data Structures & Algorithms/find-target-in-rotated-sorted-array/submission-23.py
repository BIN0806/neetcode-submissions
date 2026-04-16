class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid])
            if target == nums[mid]:
                return mid
            elif ((nums[mid] > target and target <= nums[l]) or (nums[mid] < target and target <= nums[r])):
                l = mid + 1
            else: 
                r = mid -1 

        return -1
