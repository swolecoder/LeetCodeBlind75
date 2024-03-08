from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)



        for path in paths:
            rest = path.split(" ")  
            dir= rest[0]

            for cont in rest[1:]:
                filename, content = cont.split("(")
                content = content[: -1]
                print(filename, content)
                hashMap[content].append(f"{dir}/{filename}")
        
        print(hashMap)

        return [ val for key, val in hashMap.items() if len(val) > 1]
                