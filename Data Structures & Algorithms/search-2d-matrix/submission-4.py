class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        total_area = row*col

        l, r = 0, total_area-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid // row][mid % col] == target:
                return True
            elif matrix[mid // row][mid % col] > target:
                r = mid - 1
            elif matrix[mid // row][mid % col] <target:
                l = mid + 1
        return False

        