from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque([])
        self.total = 0
        self.length = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        self.length +=1
        while self.q and len(self.q) > self.size:
            last = self.q.popleft()
            self.total -=last
            self.length -=1
        
        print(self.total, self.length)

        return self.total / self.length 

        
 


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)