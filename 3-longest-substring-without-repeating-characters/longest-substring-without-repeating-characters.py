class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashMap = {}
        left = 0
        ans = 0

        for r in range(len(s)):

            if s[r] in hashMap:
                #do soemthing
                left = max(left, hashMap[s[r]]+1)
            
            hashMap[s[r]] = r
            ans = max(ans, r - left +1)
        
        return ans


        