from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []

        i = 0

        while i < len(s):
            if s[i] != " ":
                start = i
                while i < len(s) and s[i] != " ":
                    i +=1
                
                ans.append(s[start :i])
                i -=1
            
            i +=1
        
        print(ans)
        return ' '.join(ans[::-1])

        