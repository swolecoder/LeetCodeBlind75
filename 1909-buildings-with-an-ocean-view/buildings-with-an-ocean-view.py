class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        runner = float('-inf')
        ans = []

        for i in range(len(heights)-1,-1,-1):
            if heights[i] > runner:
                ans.append(i)
            runner = max(runner, heights[i])
        return reversed(ans)
