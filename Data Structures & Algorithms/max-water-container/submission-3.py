class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n, area = len(heights), 0 
        for l in range(n):
            r = l + 1
            while (min([heights[l], heights[r]]) * r - l) > area:
                area = width*height
                r += 1 
        return area 
