class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                sub = ""

                while stack and stack[-1] != "[":
                    sub = stack.pop() + sub
                
                stack.pop()
                d = ""
                while stack and stack[-1].isdigit():
                    d = stack.pop() + d
                
                stack.append(int(d) * sub)
        return ''.join(stack)
        