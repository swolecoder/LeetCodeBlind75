class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        x,y = click 
        R = len(board)
        C = len(board[0])
        print(x,y)
        seen = set()

        if board[x][y] == "M":
            board[x][y] = "X"
            return board 

        dirs = [(0,-1),(0,1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

        def count(r,c):
            count = 0
            seen = set()
            for r1, c1 in dirs:
                new_row =r + r1
                new_col = c + c1
                if 0<=new_row < R and 0 <= new_col < C and (new_row,new_col) not in seen and board[new_row][new_col] == "M":
                    seen.add((new_row, new_col))
                    count +=1
            return count




        def dfs(r,c):
            inbound_x = 0 <=r < R
            ibound_y = 0 <= c < C

            if not inbound_x or not ibound_y or board[r][c] != "E":
                return 
            
            count_mine = count(r,c)
            # print("Ashish",count_mine)

            if count_mine > 0:
                print('RAnkan',str(count_mine))
                board[r][c] = str(count_mine)
            else:
                board[r][c] ='B'
                for r1, c1 in dirs:
                    new_row =r + r1
                    new_col = c + c1
                    if 0 <= new_row < R and 0 <= new_col < C and (new_row, new_col) not in seen and board[new_row][
                new_col] == "E":
            
                        dfs(new_row,new_col)
                        seen.add((new_row,new_col))


        dfs(x,y)
        return board

        