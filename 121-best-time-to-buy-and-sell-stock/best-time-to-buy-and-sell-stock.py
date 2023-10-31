class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        ans = 0

        for i in range(len(prices)):
            diff = prices[i] - minBuy 
            if diff >0:
                ans = max(ans, diff)
            
            minBuy = min(minBuy, prices[i])
        return ans
        