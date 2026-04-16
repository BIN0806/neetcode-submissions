class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = 1, 1
        res = [1] * n
        for i in range(0, n):
            res[i] = pre
            pre *= nums[i]
        for i in range(n-1, -1, -1):
            res[i] = res[i] * suf
            suf *= nums[i] 
        return res

        # in:  [1, 2, 3, 4]
        # res: [24, 12, 8, 6]   

        # exp: [24, 12, 8, 6]


        # in: [-1, 0, 1, 2, 3]
        # Pre: [-1, 0, 0, 0, 0]          
        # Suf: [0, 0, 6, 6, 3]
        # exp[i] = pre[i-1] * suf[i+1]
        # exp: [0, -6, 0, 0, 0]
