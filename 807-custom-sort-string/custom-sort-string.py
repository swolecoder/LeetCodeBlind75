from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map = defaultdict(int)

        for ch in s:
            map[ch] +=1
        print(map)


        res = []

        for c in order:
            if c in map:
                res.extend( c * map[c])
                del map[c]
        print(res)

        for k, v in map.items():
            res.extend((k* v))
        
        return ''.join(res)
        