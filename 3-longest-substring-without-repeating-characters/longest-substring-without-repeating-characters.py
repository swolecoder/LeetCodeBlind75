from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)
        ans = 0
        left = 0

        for right, char in enumerate(s):
            

            if char in map:
                #dop stuiff
                left = max(map[char] +1 , left)
            ans = max(ans, right - left +1)
            map[char] = right 
        return ans 

        
        