class Solution:
    def isValid(self, s: str) -> bool:

        map = {
            "(":")",
            "[":"]",
            "{":"}"
        }


        stack = []

        for i in range(len(s)):
            if s[i] in map:
                stack.append(s[i])
            else:

                if not stack:
                    return False
                if stack and map[stack.pop()] != s[i]:
                    return False
        
        return True if len(stack) == 0 else False
        