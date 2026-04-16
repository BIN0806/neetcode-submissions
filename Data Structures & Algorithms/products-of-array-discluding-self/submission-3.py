class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre, suf = 1, 1
        for i in range(1, n):
            ans[i] = nums[i-1] * pre
            pre = nums[i] * pre
        for i in range(n-2, -1, -1):
            ans[i] = ans[i] * suf
            suf = nums[i] * suf
        return ans

        # in:  [1, 2, 3, 4]
        # pre: [1, 1, 2, 6]
        # suf: [24, 12, 4, 1]
        #     
        # exp: [24, 12, 8, 6]


        # in: [-1, 0, 1, 2, 3]
        # Pre: [-1, 0, 0, 0, 0]          
        # Suf: [0, 0, 6, 6, 3]
        # exp[i] = pre[i-1] * suf[i+1]
        # exp: [0, -6, 0, 0, 0]
