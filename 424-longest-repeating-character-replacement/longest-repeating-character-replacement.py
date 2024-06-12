class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        map = defaultdict(int)
        ans = 0

        for right in range(len(s)):
            map[s[right]] = map.get(s[right], 0) +1
            while (right -left +1) - max(map.values()) > k:
                map[s[left]] -=1
                if map[left] == 0:
                    del map[left]
                left +=1
            
            
            ans = max(ans, right -left +1)
        return ans



