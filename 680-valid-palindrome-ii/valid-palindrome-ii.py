class Solution:
    def validPalindrome(self, s: str) -> bool:


        def helper(i,j):

            while i <=j:
                if s[i]!=s[j]:
                    return False
                i +=1
                j -=1
            return True
        

        l =0
        r = len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return helper(l+1,r) or helper(l, r-1)
            l +=1
            r -=1
        return True        