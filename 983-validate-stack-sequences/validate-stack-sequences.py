class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0


        for data in pushed:
            stack.append(data)
            while i < len(popped) and stack and stack[-1] == popped[i]:
                i +=1
                stack.pop()
        
        return True if len(stack) == 0 else False
