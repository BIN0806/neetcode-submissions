class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix_min = [height[0]]
        for i in range(1, n):
            prefix_min.append(max(height[i], prefix_min[i-1]))

        prefix_max = [0] * n
        prefix_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            prefix_max[i] = max(height[i], prefix_max[i+1])

        total = 0
        for r in range(n):
            print(max(min(prefix_min[r], prefix_max[r]) - height[r], 0))
            total += max(min(prefix_min[r], prefix_max[r]) - height[r], 0)

        return total 
