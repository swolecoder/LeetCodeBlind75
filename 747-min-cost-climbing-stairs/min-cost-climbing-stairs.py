class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        def helper(index, memo = {}):
            if index in memo:
                return memo[index]

            if index >= len(cost):
                return 0
            

            one_step = helper(index +1,memo)
            two_step= helper(index+2,memo)

            min_cost = cost[index] + min(one_step, two_step)
            memo[index] = min_cost

            return memo[index]
        
        ans = min(helper(0), helper(1))


        return ans
        