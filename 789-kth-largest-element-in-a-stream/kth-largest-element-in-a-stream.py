from heapq import heapify,heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minH = nums
        heapify(self.minH)
        self.k = k 

        while len(self.minH) > self.k:
            heappop(self.minH)
        

    def add(self, val: int) -> int:
        heappush(self.minH, val)
        if len(self.minH) > self.k:
            heappop(self.minH)
        return self.minH[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)