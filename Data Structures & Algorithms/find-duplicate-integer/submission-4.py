class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = nums[0]
        fast_ptr = nums[slow_ptr] 

        while True:
            if fast_ptr == slow_ptr:
                break
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]


        slow_ptr2 = nums[0]
        while True:
            if slow_ptr2 == slow_ptr:
                return slow_ptr2
            slow_ptr2 = nums[slow_ptr2]


    