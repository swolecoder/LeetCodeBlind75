class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = defaultdict(int)

        ans = 0
        left = 0

        for i in range(len(s)):
            
            if s[i] in map:
                #adjest lefdft 
                left = max(left , map[s[i]]+1)

            map[s[i]] = i
            ans = max(ans, i - left +1)

        return ans 