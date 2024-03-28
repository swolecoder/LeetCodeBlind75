class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

# Time Complexity: O(2^n).
# For every index there can be two options ‘{‘ or ‘}’. So it can be said that the upper bound of
# time complexity is O(2^n) or it has exponential time complexity.
# Space Complexity: O(n).
        def dfs(open , close, data):
            nonlocal res
            if open == close== n:
                res.append(data)
                return 
            

            if open < n:
                dfs(open +1,close, data + "(")
            
            if close < open:
                dfs(open , close +1, data +")")
            
                
            # if open == close == n:
            #     res.append("".join(stack))
            #     return 
            
            # if open < n:
            #     stack.append("(")
            #     dfs(open +1, close)
            #     stack.pop()
            
            # if close < open:
            #     stack.append(")")
            #     dfs(open, close +1)
            #     stack.pop()
        
        dfs(0,0,"")
        return res
        