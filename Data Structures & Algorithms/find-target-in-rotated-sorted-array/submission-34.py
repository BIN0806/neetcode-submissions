class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid])
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                elif nums[mid] <= nums[r]:
                    r = mid - 1

            elif target > nums[mid]:
                if nums[l] > nums[mid]:
                    r = mid - 1
                elif nums[l] <= nums[mid]:
                    l = mid + 1
        return -1
