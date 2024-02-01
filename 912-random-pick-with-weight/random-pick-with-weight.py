import random 
class Solution:

    def __init__(self, w: List[int]):
        self.total= 0
        self.sum = []
        for n in w:
            self.total += n
            self.sum.append(self.total)
        

    def pickIndex(self) -> int:
        ran = random.randint(1, self.total)
        print(ran)
        # return ran
        l = 0
        r = len(self.sum)-1
        while l <= r:
            mid = (l+r) //2
            if self.sum[mid] == ran:
                return mid
            elif self.sum[mid] > ran:
                r = mid -1
            else:
                l = mid +1
        
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()