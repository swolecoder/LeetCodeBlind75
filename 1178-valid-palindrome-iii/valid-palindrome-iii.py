class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:


        def helper(left, right,k,memo):
            key = (left, right,k)

            if key in memo:
                return memo[key]
    
            
            if left >= right:
                return True
            
            ans = None
            if s[left] == s[right]:
                ans = helper(left +1, right -1, k , memo)
            else:
                if k >0:
                    ans = helper(left+1,right, k-1,memo) or helper(left,right-1, k-1,memo)
            
            memo[key] = ans
            return memo[key]
        
        return helper(0,len(s)-1,k, {})




        