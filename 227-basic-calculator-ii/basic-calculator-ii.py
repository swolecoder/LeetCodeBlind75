class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        s += "+"
        stack = []
        curr = ""


        for i in range(len(s)):
            if s[i].isdigit():
                curr += s[i]
                i +=1
            elif s[i] in ["+","-","*","/"]:
                if sign == "+":
                    stack.append(int(curr))
                elif sign == "-":
                    stack.append(-1 * int(curr))
                elif sign == "*":
                    last = stack.pop()
                    stack.append(last * int(curr))
                else:
                    last = stack.pop()

                    if last // int(curr) < 0 and (last % int(curr)) != 0:
                        stack.append(last // int(curr) + 1)
                    else:
                        stack.append(last // int(curr))

                
                curr = ""
                sign = s[i]

        print(stack)
        return sum(stack)

        