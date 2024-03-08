from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        map = Counter(nums)
        print(map)
        res = []



        def dfs( data):
            nonlocal res
            if len(data) == len(nums):
                res.append(data.copy())
                data.pop()
                return 
            

            for key in map:
                if map[key] > 0:
                    map[key] -=1
                    dfs(data + [key])

                    map[key] +=1
                    
        
        dfs([])
        return res




        