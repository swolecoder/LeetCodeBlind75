class Solution:
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height)-1
        ans = 0

        while i < j:

            find_height = min(height[i], height[j])
            ans = max(ans ,find_height * (j-i))
            print(ans)

            if height[i] > height[j]:
                j -=1
            else:
                i +=1
        return ans 

        