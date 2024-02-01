class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack = []
        # listS = list(s)

        # for i in range(len(listS)):
        #     if listS[i] == "(":
        #         stack.append(i)
        #     elif listS[i] ==")":
        #         if stack:
        #             stack.pop()
        #         else:
        #             listS[i] = ""

        # for i in range(len(stack)):
        #     listS[stack[i]] = ""
        
        # return ''.join(listS)

        count = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                count +=1
            elif s[i] == ")":
                if count == 0:
                    s[i] = ""
                else:
                    count -=1
        for i in range(len(s)-1,-1,-1):
            if s[i] == "(" and count > 0:
                s[i] = ""
                count -=1
        return ''.join(s)
        
        