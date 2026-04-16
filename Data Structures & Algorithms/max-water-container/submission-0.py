class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n, area = len(heights), 0 
        for l in range(n):
            for r in range(l + 1, n):
                heights = min(heights[l], heights[r])
                width = r - l 
                area = max(area, width*heights )
        return area 
