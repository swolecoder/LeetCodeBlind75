class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        map = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            map[s[i]] = 1+ map.get(s[i], 0)
        print(map)
        for i in range(len(t)):

            if t[i] not in map or map[t[i]] < 0:
                print(t[i],map)
                return False
            
            map[t[i]] = map.get(t[i],0) -1
        print(map)
        
        for key, val in map.items():
            if val > 0:
                return False
        return True