from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)


        for index, word in enumerate(strs):
            data = [0] * 26
            for i in range(len(word)):
                data[ord(word[i]) - ord('a')] +=1
            
            map[tuple(data)].append(word)
        
        print(map)

        return map.values()
        