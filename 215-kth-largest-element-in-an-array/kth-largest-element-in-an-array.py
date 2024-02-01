from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [ -1 * num for num in nums]

        heapify(h)

        k = k -1
        while k and h:
            heappop(h)
            k -=1
        
        return -1 * heappop(h) if len(h) > 0 else -1
        