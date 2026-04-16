class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, area = 0, len(heights) - 1, 0 

        while l < r:
            area = max(area, (r-l) * min(heights[l], heights[r]))
            # l is bottle neck
            if heights[r] >= heights[l]:
                l += 1
             # r is bottle neck 
            elif heights[r] <= heights[l]:
                r -= 1
            # not sure
            else: 
                continue
        return area 
