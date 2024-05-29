from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        if len(s) != len(t):
            return False

        for ch in s:
            hashMap[ch] = hashMap.get(ch,0) +1
        print(hashMap)

        for ch in t:
            if ch not in hashMap:
                return False
            hashMap[ch] = hashMap.get(ch,0) -1

            if hashMap[ch]  <= 0:
                del hashMap[ch]
        
        return True 

        
        