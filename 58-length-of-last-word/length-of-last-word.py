class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip().split(" ")
        # return len(s[-1])

        ans = 0
        i = len(s)-1


        while s[i] == " " and i >= 0:
            i -=1
        
        while s[i] != " " and i >= 0:
            ans +=1
            i -=1
        
        return ans

        