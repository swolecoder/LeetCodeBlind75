from collections import defaultdict
from heapq import heappush, heappop, heapify
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = 1
        ans = [0] * n
        map = defaultdict(int)
       

        for index, d in enumerate(sorted(arr)):
            if d  not in map:
                map[d] = n
                n +=1
        print(map)

        for i in range(len(arr)):
            arr[i] = map[arr[i]]
        
        return arr

 




        