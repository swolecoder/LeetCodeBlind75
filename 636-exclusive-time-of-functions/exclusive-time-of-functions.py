class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []

        for log in logs:
            index, code, time = log.split(":")

            if code == "start":
                stack.append([int(index),int(time)])
            else:
                i, t = stack.pop()
                cal = int(time) - t  + 1
                
                if stack:
                   ans[stack[-1][0]] -= cal
                ans[i] += cal
        
        return ans 

        
