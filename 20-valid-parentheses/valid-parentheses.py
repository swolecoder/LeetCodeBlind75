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
                
                lastVal = stack.pop()
                if  map[lastVal] != s[i]:
                    return False
        
        return False if len(stack) > 0 else True

        