class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):

            total = 0

            for pile in piles:
                total += ceil(pile/k) 
            
            return total <= h


        
        i = 1
        j = max(piles)

        while i <= j:
            middle = ( i +j) //2

            if check(middle):
                j = middle -1
            else:
                i = middle +1
        
        return i
        