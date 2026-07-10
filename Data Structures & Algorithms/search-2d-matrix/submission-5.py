class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r,w = 0, len(matrix) - 1, len(matrix[0]) - 1
        while l <= r:
            halfway = (l + r) // 2
            row = matrix[halfway]

            if row[0] <= target <= row[w]:
                inner_l, inner_r = 0, w
                while inner_l <= inner_r:
                    inner_halfway = (inner_l + inner_r) // 2
                    if row[inner_halfway] == target:
                        return True
                    elif row[inner_halfway] < target:
                        inner_l = inner_halfway + 1
                    else:
                        inner_r = inner_halfway - 1
                return False
            elif target < row[0]:
                r = halfway - 1
            else:
                l = halfway + 1
        return False