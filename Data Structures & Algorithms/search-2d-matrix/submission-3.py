class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r,w = 0, len(matrix) - 1, len(matrix[0]) - 1

        while l <= r:
            halfway = (r + l) // 2
            if target >= matrix[halfway][0] and target <= matrix[halfway][w]:
                inner_l, inner_r = 0, w
                while inner_l <= inner_r:
                    inner_halfway = (inner_r + inner_l) // 2
                    if target == matrix[halfway][inner_halfway]:
                        return True
                    elif target < matrix[halfway][inner_halfway]:
                        inner_r = inner_halfway - 1
                    else:
                        inner_l = inner_halfway + 1
                return False
            elif target < matrix[halfway][0]:
                r = halfway - 1
            else:
                l = halfway + 1

        return False