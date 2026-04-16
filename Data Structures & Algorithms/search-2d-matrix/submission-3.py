class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        mid_r = -1 
        l, r = 0, row-1
        while l <= r:
            mid_r = (r+l) // 2
            if matrix[mid_r][0] == target:
                return True
            elif matrix[mid_r][0] < target:
                l = mid_r + 1
            else:
                r = mid_r - 1
        mid_r = r

        mid_c = -1 
        l, r = 0, col-1
        while l <= r:
            mid_c = (r+l) // 2
            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                l = mid_c + 1
            else:
                r = mid_c - 1

        return matrix[mid_r][mid_c] == target
            

        