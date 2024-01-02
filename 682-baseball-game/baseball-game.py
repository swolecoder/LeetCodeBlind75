class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []


        for o in operations:
            if o == "+":
                first = stack[-2] 
                second = stack[-1]

                stack.append(first + second)
            elif o =="D":
                last = stack[-1]
                stack.append(last * 2)
            elif o == "C":
                stack.pop()
            else:
                stack.append(int(o))
        

        print(stack)

        return sum(stack)