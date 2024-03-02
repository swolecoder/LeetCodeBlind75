class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        
        for char in s:
            if char == "(":
                stack.append(0)  # Push 0 to represent a new balanced pair
            else:
                # Pop the stack until a 0 is encountered which represents '('
                score = 0
                while stack[-1] != 0:
                    score += stack.pop()
                stack.pop()  # Pop the 0
                # If score is 0, it means it was an empty pair "()", so add 1. 
                # Otherwise, double the score found between the parentheses.
                stack.append(max(2 * score, 1))
                
        # Sum up everything left in the stack to get the final score
        return sum(stack)

        