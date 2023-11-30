from heapq import heappush,heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = [-num for num in nums]
        heapify(h)

        n = k-1



        while n and h:
            heappop(h)
            n -=1
        

        return -1 if len(h) == 0 else -1 * heappop(h)
        