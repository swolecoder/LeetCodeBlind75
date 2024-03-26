class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        r, c = len(board), len(board[0])
        todo = True

        while todo:
            todo = False
            # Mark candies to be crushed horizontally
            for i in range(r):
                for j in range(c - 2):
                    val = abs(board[i][j])
                    if val != 0 and val == abs(board[i][j + 1]) and val == abs(board[i][j + 2]):
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -val
                        todo = True

            # Mark candies to be crushed vertically
            for j in range(c):
                for i in range(r - 2):
                    val = abs(board[i][j])
                    if val != 0 and val == abs(board[i + 1][j]) and val == abs(board[i + 2][j]):
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -val
                        todo = True

            # Crush candies
            for i in range(r):
                for j in range(c):
                    if board[i][j] < 0:
                        board[i][j] = 0

            # Apply gravity
            for j in range(c):
                idx = r - 1
                for i in range(r - 1, -1, -1):
                    if board[i][j] > 0:
                        board[idx][j] = board[i][j]
                        if i != idx:
                            board[i][j] = 0
                        idx -= 1

        return board
