class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r,w = 0, len(matrix) - 1, len(matrix[0]) - 1

        while l <= r:
            halfway = (r + l) // 2
            if target >= matrix[halfway][0] and target <= matrix[halfway][w]:
                for num in matrix[halfway]:
                    if num == target:
                        return True
                return False
            elif target < matrix[halfway][0]:
                r = halfway - 1
            else:
                l = halfway + 1

        return False