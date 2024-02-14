class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minTracker = prices[0]
        
        ans = 0

        for i in range(len(prices)):
            diff = prices[i] - minTracker
            ans = max(diff, ans)
            minTracker = min(minTracker,prices[i])
        return ans