class Solution:
    # O(n*m) dfs 4 ^ len(word)
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        path = set()

        def dfs(r,c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROW or c >=COL or (r,c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r,c))

            res = dfs(r+1,c, i+1) or  dfs(r,c+1, i+1) or  dfs(r-1,c, i+1) or  dfs(r,c-1, i+1)
            path.remove((r,c))
            return res
        

        for i in range(ROW):
            for j in range(COL):
                if dfs(i,j,0):
                    return True
        return False
   


            



