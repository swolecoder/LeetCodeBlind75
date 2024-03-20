
class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        minimum = min(val, self.stack[-1][1])if self.stack else val
        self.stack.append((val,minimum))
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()