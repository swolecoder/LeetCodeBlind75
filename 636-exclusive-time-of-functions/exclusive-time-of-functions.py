class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = deque()
        ans = [0] * n

        for log in logs:
            id, name, time = log.split(":")

            if name == "start":
                stack.append((int(id), int(time)))
            else:
                id1,lastTime = stack.pop()
                cal = int(time) +1 - lastTime
                print(cal,time, lastTime)
                if stack:
                   ans[stack[-1][0]] -= cal
                ans[id1] += cal
        print(ans)

        return ans


    # "0:start:0","1:start:2","1:end:5","0:end:6"]
          



