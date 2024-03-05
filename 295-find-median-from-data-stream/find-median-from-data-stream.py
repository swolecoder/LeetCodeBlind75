from heapq import heappush , heappop, heapify
class MedianFinder:

    def __init__(self):
        self.max = []
        self.min = []

        

    def addNum(self, num: int) -> None:
        #bit eempty
        if not self.max or num <= -1* self.max[0]:
            heappush(self.max,-1* num)
        else:
            heappush(self.min, num)
        
        if len(self.max) - len(self.min) > 1:
            popData = heappop(self.max)
            heappush(self.min,-1 * popData)
        elif len(self.min) - len(self.max) > 1:
            popData = heappop(self.min)
            heappush(self.max,-1 * popData)

    def findMedian(self) -> float:
        if len(self.max) > len(self.min):
            return -self.max[0]
        elif len(self.max) < len(self.min):
            return self.min[0]
        else:
            return (-self.max[0] + self.min[0]) / 2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()