class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 1
        for num in nums:
            count = 1 
            while (num - 1) in nums:
                count += 1
                num -= 1
            best = max(count, best)
        return best

        [2, 20, 4, 10, 3, 4, 5]
        nums = (2, 20, 4, 10, 3, 5)
        best = 1
        count = 3
        num = 2