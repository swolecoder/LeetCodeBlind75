class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1 _> 2, 3 Live neigboutrr other ise it will die
        # 0 -> Live if it has exsaaacrtly 3 nightbouit  will become aklive otherwise deaD
        

        n = len(board)
        m = len(board[0])

        dirs = [
            (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
            ]
        map = {
            (0, 0): 0, 
            (1, 0): 1, 
            (0, 1): 2,
            (1, 1): 3
        }

        def count(i,j):
            count = 0

            for x,y in dirs:
                x1 = x + i 
                y1 = y + j

                in_bound_x = 0 <= x1 < n
                in_bound_y = 0 <= y1 < m

                if in_bound_x and in_bound_y and (board[x1][y1] == 1 or board[x1][y1]== 3):
                    count +=1
            return count 


            
        
        # next state 
        def next_state(i,j):
            current_state = board[i][j]
            total_count = count(i,j)
            next_state = 0
            
            if current_state == 1:
                if total_count == 2 or  total_count == 3:
                    next_state = 1
            elif current_state == 0 and total_count == 3:
                next_state = 1
            
            key = (current_state, next_state)
            board[i][j] = map[key]
        
        for i in range(n):
            for j in range(m):
                next_state(i,j)

              
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 3 or board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] ==1:
                    board[i][j] =0
        

