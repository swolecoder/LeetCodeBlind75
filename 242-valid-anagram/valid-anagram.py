class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}

        if len(s)!= len(t): return False

        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
        
        for j in range(len(t)):

            map[t[j]] = map.get(t[j], 0) -1

            if map[t[j]] <= 0:
                del map[t[j]]
        

    
        
        print(map)

        return True if len(map.keys()) <= 0 else False
        