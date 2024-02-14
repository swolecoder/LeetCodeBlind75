from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for path in paths:
            # print(path)
            
            splitData = path.split(" ")
            root = splitData[0]
            for data in splitData[1:]:
                # print(data)
                file_name, content = data.split("(")
                # print(data)
                print(file_name, content[:-1])
                map[content[:-1]].append(f"{root}/{file_name}")
        print(map)

        return [ value for value in map.values() if len(value) > 1]
                