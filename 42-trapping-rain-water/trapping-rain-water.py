class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        ans = 0

        while l < r:
            if height[l] < height[r]:
                # Update maxL to the highest seen so far from the left
                maxL = max(maxL, height[l])
                # Calculate trapped water at l based on the updated maxL
                water = maxL - height[l]
                ans += water
                # Then, move l towards the center
                l += 1
            else:
                # Update maxR to the highest seen so far from the right
                maxR = max(maxR, height[r])
                # Calculate trapped water at r based on the updated maxR
                water = maxR - height[r]
                ans += water
                # Then, move r towards the center
                r -= 1

        return ans

            