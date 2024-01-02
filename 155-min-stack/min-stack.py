class MinStack:

    def __init__(self):
        # first on will be val and secodnd one will be min
        self.stack = deque()
        

    def push(self, val: int) -> None:
        minimum = min(self.stack[-1][1],val) if self.stack else val
        self.stack.append((val, minimum))
        

    def pop(self) -> None:
        lastElement = self.stack.pop()
        return lastElement[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()