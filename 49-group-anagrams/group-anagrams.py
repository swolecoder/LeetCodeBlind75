from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for word in strs:
            sort = [0] * 26
            for j in range(len(word)):
                 key  = ord(word[j]) - ord('a')
                 sort[key] +=1
            map[tuple(sort)].append(word)
        return map.values()

        