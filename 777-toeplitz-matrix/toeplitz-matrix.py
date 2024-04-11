from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        map = defaultdict(int)

        R = len(matrix)
        C = len(matrix[0])

        for r in range(R):
            for c in range(C):
                key = c - r
                if key in map:
                    val = map[key]
                    if val != matrix[r][c]:
                        return False
                else:
                    map[key] = matrix[r][c]
        
        return True
        