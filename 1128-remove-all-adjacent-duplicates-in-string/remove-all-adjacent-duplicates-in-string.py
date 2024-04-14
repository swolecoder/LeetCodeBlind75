class Solution:
    def removeDuplicates(self, s: str) -> str:


        # "abbaca"

        stack = []

        for index, ch in enumerate(s):

            if stack and  ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        
        print(stack)
        return ''.join(stack)




        