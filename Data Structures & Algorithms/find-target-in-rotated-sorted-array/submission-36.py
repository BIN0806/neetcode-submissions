class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid, nums[mid])

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                if nums[mid] <= nums[r] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            elif target > nums[mid]:
                if nums[l] <= nums[mid] and target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
