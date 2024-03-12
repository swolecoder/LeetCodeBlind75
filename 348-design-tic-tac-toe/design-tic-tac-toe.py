from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        val = 1 if player == 1 else -1

        # Update row and column counts
        self.row[row] += val
        self.col[col] += val

        # Check for winning condition in row and column
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n:
            return player

        # Update diagonal and anti-diagonal counts if applicable
        if row == col:
            self.diag += val
        if row + col == self.n - 1:
            self.anti_diag += val

        # Check for winning condition in diagonal and anti-diagonal
        if abs(self.diag) == self.n or abs(self.anti_diag) == self.n:
            return player

        # No winning condition reached
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)