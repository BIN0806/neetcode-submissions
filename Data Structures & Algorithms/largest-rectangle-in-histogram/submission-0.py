class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best_area = 0 
        stack = [] # (idx, height)
        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                width = i - index
                best_area = max(width*height, best_area)
                start = index
            stack.append((start, h))
   
        for i, h in stack:
            width = len(heights) - i
            best_area = max(width*h, best_area)
        return best_area