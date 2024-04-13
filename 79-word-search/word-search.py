class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])

        def dfs(index, r, c, seen):
            if index == len(word):
                return True

            if not (0 <= r < R) or not (0 <= c < C) or (r, c) in seen or word[index] != board[r][c]:
                return False
            
            seen.add((r, c))
            
            if (dfs(index + 1, r - 1, c, seen) or
                dfs(index + 1, r, c - 1, seen) or
                dfs(index + 1, r + 1, c, seen) or
                dfs(index + 1, r, c + 1, seen)):
                return True
            
            # Backtrack
            seen.remove((r, c))
            return False

        for i in range(R):
            for j in range(C):
                if dfs(0, i, j, set()) and board[i][j] == word[0]:
                    return True
        return False
