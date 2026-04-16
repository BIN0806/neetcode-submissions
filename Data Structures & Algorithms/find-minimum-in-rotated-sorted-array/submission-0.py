class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, smallest = 0, len(nums)-1, 1001
        while l <= r:
            mid = (l+r)//2
            print("pre:", l, mid, r, smallest, nums[l:r+1])
            smallest = min(nums[mid], smallest)
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] <= nums[r]: 
                r = mid - 1
            print("post:", l, mid, r, smallest, nums[l:r+1])
        return smallest