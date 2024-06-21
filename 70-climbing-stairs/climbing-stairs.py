class Solution:
    def climbStairs(self, n: int) -> int:
        map = {}
        def helper(n):

            if n in map:
                return map[n]

            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            ans = helper(n-1) + helper(n-2)
            map[n] = ans
            return map[n]
        return helper(n)

