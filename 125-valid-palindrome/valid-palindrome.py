class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) -1

        while i < j:
            while i < j and i < len(s) and not  s[i].isalnum():
                i +=1
            while j > i and j > 0 and not s[j].isalnum():
                j -=1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i +=1
            j -=1
        
        return True 