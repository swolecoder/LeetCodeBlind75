class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        left_max = float("-inf")


        ans = []

        for i in range(len(heights)-1,-1,-1):
            if heights[i] > left_max:
                ans.append(i)
            left_max = max(left_max, heights[i])
        
        return ans[::-1]
        