class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for d in s:
            if d == "*" and stack:
                stack.pop()
            else:
                print(d)
                stack.append(d)
        return ''.join(stack)
