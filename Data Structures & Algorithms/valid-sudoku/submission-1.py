class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku_row = defaultdict(list)
        sudoku_col = defaultdict(list)
        sudoku_square = defaultdict(list)
        for i in range(len(board)):
            for j in range(len(board)):
                current_tile = board[i][j]
                if current_tile == ".":
                    continue
                if current_tile in sudoku_row[i] or current_tile in sudoku_col[j] or current_tile in sudoku_square[(i // 3, j // 3)]:
                    return False
                sudoku_row[i].append(current_tile)
                sudoku_col[j].append(current_tile)
                sudoku_square[(i // 3, j // 3)].append(current_tile)

        return True
