from collections import deque
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''
        R = len(board)
        C = len(board[0])
        for r in range(R):
            for c in range(C):
                start += str(board[r][c])

        print(start)
        final = '123450'
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        q = deque([(start,0)])
        visited = set()
        visited.add(start)

        while q:

            node , level = q.popleft()
            if node == final:
                return level
            
            zeroIndex = node.index('0')

            for nei in neighbors[zeroIndex]:
                data = list(node)
                data[zeroIndex], data[nei] =data[nei] , data[zeroIndex]

                new_state = ''.join(data)
                if new_state not in visited:
                    q.append((new_state, level +1))
                    visited.add(new_state)
        return -1






        