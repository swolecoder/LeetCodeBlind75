class Solution:
    def longestPalindrome(self, s: str) -> str:
        

        ans = ""
        maxLength = 0

        for r in range(len(s)):
            left = r
            right = r

            while left >=0 and right < len(s) and s[left] == s[right]:

                l = right - left + 1
                if l >= maxLength:
                    maxLength= l
                    ans = s[left: right +1]
                left -=1
                right +=1
            
            left = r
            right = r +1

            while left >=0 and right < len(s) and s[left] == s[right]:
                l = right - left + 1
                if l >= maxLength:
                    maxLength = l
                    ans = s[left: right +1]
                
                left -=1
                right +=1
        
        return ans

