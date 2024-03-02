from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(data):
            res = []
            for i in range(4):
                d1 = (int(data[i]) + 1) % 10
                s1 = data[:i] + str(d1) + data[i + 1:]
                res.append(s1)
                d2 = (int(data[i]) - 1 + 10) % 10
                s2 = data[:i] + str(d2) + data[i + 1:]
                res.append(s2)
            return res

        if '0000' in deadends:
            return -1

        q = deque([('0000', 0)])
        seen = set('0000')

        while q:
            node, step = q.popleft()
            if node == target:
                return step
            
            for child in children(node):
                if child not in seen and child not in deadends:
                    seen.add(child)
                    q.append((child, step + 1))

        return -1  # Return -1 if the target is not reachable
