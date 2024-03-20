from collections import Counter
from heapq import heappush, heappop,heapify
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        print(map)
        data  = [ (val, key) for key, val in map.items()]
        
        heapify(data)
        print(data)
        while len(data) > k:
            heappop(data)

        print(data)
        return [num for(fre, num ) in data]