class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        mis = 0
        for ch in s:
            if ch == "]":
                mis +=1
            else:
                mis -=1
            ans = max(ans, mis)



        return ceil(ans/2)
        