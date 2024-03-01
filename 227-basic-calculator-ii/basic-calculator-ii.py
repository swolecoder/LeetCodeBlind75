class Solution:
    def calculate(self, s: str) -> int:
        sign ="+"
        s += "+"
        curr  = 0
        stack = []


        for i in range(len(s)):
            if s[i] == " ":
                continue
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            elif s[i] in ["*","/","+","-"]:
                if sign == "+":
                    stack.append(curr)
                elif sign =="-":
                    stack.append(-1* curr)
                elif sign == "*":
                    last = stack.pop()
                    stack.append(last * curr)
                else:
                    last = stack.pop()
                    if last // curr < 0 and last % curr != 0:
                        stack.append(last // curr + 1)
                    else:
                        stack.append(last // curr)
                
                sign = s[i]
                curr = 0
        print(stack)

        return sum(stack)







