class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        listS = list(s)

        for i in range(len(listS)):
            if listS[i] == "(":
                stack.append(i)
            elif listS[i] ==")":
                if stack:
                    stack.pop()
                else:
                    listS[i] = ""

        for i in range(len(stack)):
            listS[stack[i]] = ""
        
        return ''.join(listS)
        
        