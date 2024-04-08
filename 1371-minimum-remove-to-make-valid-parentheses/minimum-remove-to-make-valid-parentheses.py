class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        s = list(s)
        print(s)

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        print(stack)
        
        for data in stack:
            s[data] = ""
        
        return ''.join(s)
        