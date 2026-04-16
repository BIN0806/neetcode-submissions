class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for num in nums:
            if (num-1) not in nums:
                count = 1 
                while (num + 1) in nums:
                    count += 1
                    num += 1
                best = max(count, best)
        return best
