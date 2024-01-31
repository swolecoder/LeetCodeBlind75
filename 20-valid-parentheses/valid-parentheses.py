class Solution:
    def isValid(self, s: str) -> bool:

        map = {
            "(":")",
            "[":"]",
            "{":"}"
        }

        stack = []

        for n in s:
            if n in map:
                stack.append(n)
            else:
                if not stack:
                    print("I am here")
                    return False
                last = stack.pop()
                if  map[last] != n:
                    return False
        print(stack)
        return len(stack) == 0
        