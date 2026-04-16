class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        mid_r = -1 
        l, r = 0, row-1
        while l <= r:
            mid_r = (r+l) // 2
            print("pre left:", l, "mid_r:", mid_r, "right:", r)
            if matrix[mid_r][0] == target:
                return True
            elif matrix[mid_r][0] < target:
                l = mid_r + 1
            else:
                r = mid_r - 1
            print("post left:", l, "mid_r:", mid_r, "right:", r)
        # mid_r should now be at row we are looking for
        mid_r = r
        print(mid_r)

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
            print("left:", l, "mid_c:", mid_c, "right:", r)
        # mid_c = 1 if l == r else 0

        print(mid_r, mid_c, matrix[mid_r][mid_c])
        return matrix[max(mid_r, 0)][max(mid_c, 0)] == target
            

        