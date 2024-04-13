class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        r, endRow = 0, len(matrix)
        c, endCol = 0, len(matrix[0])

        while r < endRow and c < endCol:
            # Process top row
            for i in range(c, endCol):
                ans.append(matrix[r][i])

            r += 1

            # Process right column
            for i in range(r, endRow):
                ans.append(matrix[i][endCol - 1])

            endCol -= 1

            # Process bottom row
            if r < endRow:
                for i in range(endCol - 1, c - 1, -1):
                    ans.append(matrix[endRow - 1][i])

                endRow -= 1

            # Process left column
            if c < endCol:
                for i in range(endRow - 1, r - 1, -1):
                    ans.append(matrix[i][c])

                c += 1

        print(ans)
        return ans 



        