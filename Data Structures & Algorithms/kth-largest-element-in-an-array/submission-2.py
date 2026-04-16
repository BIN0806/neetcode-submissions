class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = len(nums) - k
        def quickselect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == idx: return nums[p]
            if p > idx: return quickselect(l, p-1)
            if p < idx: return quickselect(p+1, r)
                
        return quickselect(0, len(nums)-1)
