class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = { w : i for i,w in enumerate(order)}
        print(map)
        map[""] = -1
        
        for i in range(len(words)-1):
            curr = words[i]
            next = words[i+1]

            for j in range(len(curr)):

                if j == len(next):
                    return False

                if curr[j] == next[j]:
                    continue
                else:

                    if map[next[j]] > map[curr[j]]:
                        break
                    else:
                        return False
        return True 