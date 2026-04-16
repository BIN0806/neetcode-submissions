class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        def backtrack(lst, pick):
            if len(lst) == n:
                res.append(lst)
                return 

            for i in range(n):
                if not pick[i]:
                    pick[i] = True
                    backtrack(lst + [nums[i]], pick)
                    pick[i] = False

        backtrack([], [False] * n)
        return res