import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)

        for i in range(len(strs)):
             key = [0] * 26

             for j in range(len(strs[i])):
                 key[ord(strs[i][j]) - ord('a')] +=1
             
             hashMap[tuple(key)].append(strs[i])
        
        print(hashMap)
        return hashMap.values()