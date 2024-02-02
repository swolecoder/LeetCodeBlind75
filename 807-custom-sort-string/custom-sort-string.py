import collections
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashMap = collections.defaultdict(int)
        for ch in s:
            hashMap[ch] +=1
        
        print(hashMap)
        ans = []

        for ch in order:
            if ch in hashMap:
                ans.extend((ch * hashMap[ch]))
                del hashMap[ch]
        print(ans)

        for k, v in hashMap.items():
            ans.extend((k*v))
        
        return ''.join(ans)

        