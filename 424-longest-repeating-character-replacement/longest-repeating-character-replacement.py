class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        l = 0
        res = 0

        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1

            if (i - l +1) - max(map.values()) > k:
                map[s[l]] = map[s[l]] -1
                l +=1
            
            res = max(res, i-l +1)
        return res 
        