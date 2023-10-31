class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        map = {}

        ans = 0
        l =0

        for r in range(len(s)):
            if s[r] in map:
                l = max(l, map[s[r]]+ 1)

            map[s[r]] = r
            ans = max(ans, r-l +1)
        
        return ans




        

        