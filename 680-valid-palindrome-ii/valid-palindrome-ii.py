class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l,r):

            while l <= r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True
        
        l, r= 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return helper(l,r -1) or helper(l+1,r)
            l +=1
            r -=1
        return True
        