class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidRow(row):
                return False
        for i in range(len(board)):
            if not self.isValidCol(board, i):
                return False
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                if not self.isValidSquare(board, [i,j]):
                    return False
        return True

    def isValidRow(self, row: List[str]) -> bool:
        counter = defaultdict(int)
        for c in row:
            if counter[c] == 1 and c != '.':
                return False
            counter[c] += 1
        return True

    def isValidCol(self, board: List[List[str]], col_number: int) -> bool:
        counter = defaultdict(int)
        for i in range(len(board)):
            if counter[board[i][col_number]] == 1 and board[i][col_number] != '.':
                return False
            counter[board[i][col_number]] +=1
        return True
        
    def isValidSquare(self, board: List[List[str]], start_point: tuple(int, int)) -> bool:
        counter = defaultdict(int)
        for i in range(start_point[0], start_point[0] + 3):
            for j in range(start_point[1], start_point[1] + 3):
                if counter[board[i][j]] == 1 and board[i][j] != '.':
                    return False
                counter[board[i][j]] += 1
        return True
