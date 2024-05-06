class Solution:
    def trap(self, height: List[int]) -> int:
        left, maxL = 0, height[0]
        right, maxR = len(height) -1 , height[len(height)-1]
        ans = 0

        while left < right:

            if maxL <= maxR:
                left +=1
                maxL = max(maxL, height[left])
                ans += maxL - height[left]
            else:
                right -=1
                maxR= max(maxR, height[right])
                ans += maxR- height[right]
               
            
        return ans
        