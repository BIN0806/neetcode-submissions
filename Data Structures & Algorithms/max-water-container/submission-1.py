class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n, area = len(heights), 0 
        for l in range(n):
            for r in range(l + 1, n):
                compare = [heights[l], heights[r]]
                height = min(compare)
                width = r - l 
                area = max(area, width*height)
        return area 
