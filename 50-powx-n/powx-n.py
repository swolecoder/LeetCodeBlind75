class Solution:
    def myPow(self, x: float, n: int) -> float:

        # 2 ^ 10 = 2 ^ 5 * 2^ 5

        # 2 ^ 5 = 2 * 2 ^ 4

        # 2 ^ 4 = 2 ^ 2 * 2 ^ 2

        # 2 ^2=2 ×2

        # 2 ^ 1 = 2 
        # 2 ^ 0 = 1

        def helper(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                temp = helper(x , n//2)
                return temp * temp
            else:
                return x * helper(x,n-1)
        
        if n < 0:
            return 1/ helper(x, abs(n))
        else:
            return helper(x,n)


        