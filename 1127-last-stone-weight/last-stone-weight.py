from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        s = [-1 * stone for stone in stones]

        heapify(s)

        while len(s) > 1:
            first = heappop(s)
            second = heappop(s)

            if abs(first)> abs(second):

                heappush(s, -1 * (abs(first)- abs(second)))
        
        return  0 if len(s) == 0 else -1 * s[0]
        