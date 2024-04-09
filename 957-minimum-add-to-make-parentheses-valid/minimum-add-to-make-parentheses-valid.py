class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        # stack = []
        count = 0
        extra = 0
        # "()))(("

        # count = 0
        # extra = 2

        for br in s:
            if br == "(":
                count +=1
            else:
                if count > 0:
                    count -=1
                else:
                    extra +=1
        
        return extra + count 
        