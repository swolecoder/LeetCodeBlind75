from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r = deque()
        d = deque()
        s = list(senate)

        for i, c in enumerate(s):
            if c == "D":
                d.append(i)
            else:
                r.append(i)
            
        while r and d:
            a = d.popleft()
            b = r.popleft()

            if a < b:
                d.append(a + len(senate))
            else:
                r.append(b + len(senate))
        return 'Radiant' if r else 'Dire'