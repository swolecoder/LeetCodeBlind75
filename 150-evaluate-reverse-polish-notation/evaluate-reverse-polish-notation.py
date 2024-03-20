class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(token)
            if token == "+":
                first = stack.pop()
                second = stack.pop()

                stack.append(first + second)
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second -first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(first  * second)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first))
            else:
                stack.append(int(token))

        return stack[-1]