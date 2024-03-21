from heapq import heappush, heappop, heapify
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        R = len(mat)
        C = len(mat[0])

        h = []
        heapify(h)

        for r in range(R):
            count = 0
            for c in range(C):
                if mat[r][c] == 1:
                    count +=1
            
            print(f"{r}:{count}")
            heappush(h,(count,r))
        print(h)

        ans = []
        while h and k:
            count, r = heappop(h)
            ans.append(r)
            k -=1
        return ans
        