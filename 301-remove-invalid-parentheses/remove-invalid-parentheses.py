from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def balace(data):
            count = 0

            for d in data:
                if d == "(":
                    count +=1
                elif d == ")":
                    if not count:
                        return False
                    count -=1
            return count == 0
        

        stack = deque([s])
        found = False
        res = []
        visited = set()

        while stack:
            data = stack.popleft()

            if balace(data):
                res.append(data)
                found = True
            
            if found:
                continue 
            
            for j in range(len(data)):
                if data[j] in "()":
                    new_data = data[:j] + data[j+1:]
                    if new_data not in visited:
                        visited.add(new_data)
                        stack.append(new_data)
        return res 


        