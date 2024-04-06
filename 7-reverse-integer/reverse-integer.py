class Solution:
    def reverse(self, x: int) -> int:
        

        negative = False

        if x < 0:
            negative = True
            x = x * -1
        

        res = 0

        maxNumber = 2 ** 31 -1
        minNumber = -1 * 2 ** 31

        while x > 0:

            res = res * 10 + ( x % 10)

            x = x // 10
        
        if res > maxNumber:
            return 0
        

        return res * -1  if negative else res