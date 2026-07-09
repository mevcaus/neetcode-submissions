class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r,w = 0, len(matrix) - 1, len(matrix[0]) - 1
        while l <= r:
            halfway = (l + r) // 2
            if matrix[halfway][0] <= target and matrix[halfway][w] >= target:
                inner_l,inner_r = 0, w
                while inner_l <= inner_r:
                    inner_half = (inner_l + inner_r) // 2
                    if target == matrix[halfway][inner_half]:
                        return True
                    elif target < matrix[halfway][inner_half]:
                        inner_r = inner_half - 1
                    else:
                        inner_l = inner_half + 1
                return False
            elif matrix[halfway][0] > target:
                r = halfway - 1
            else:
                l = halfway + 1

        return False