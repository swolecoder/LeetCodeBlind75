from heapq import heapify, heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = [ -num for num in nums]
        heapify(h)

        k = k -1

        while h and k:
            print(k)
            heappop(h)
            k -=1
        print(h)
        
        return -1 * heappop(h) if h else -1
        
        