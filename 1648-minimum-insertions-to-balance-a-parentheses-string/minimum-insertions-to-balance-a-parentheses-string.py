class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        count = 0

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
                i +=1
            else:
                if not stack:
                    if i + 1 < len(s) and s[i + 1] == ")":
                        count += 1
                        i += 2
                    else:
                        count += 2  # Insert a missing opening bracket
                        i += 1
                else:
                    if i + 1 < len(s) and s[i + 1] == ")":
                        i += 2
                    else:
                        count += 1  # Insert a missing opening bracket
                        i += 1
                    stack.pop()

        # Add remaining unmatched opening brackets
        ans = len(stack) * 2  # Two closing brackets are needed for each unmatched opening bracket
        return ans + count
