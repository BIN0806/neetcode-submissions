class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, area = 0, len(heights) - 1, 0 

        while l < r:
            area = max(area, (r-l) * min(heights[l], heights[r]))
            if heights[r] >= heights[l]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
        return area 
