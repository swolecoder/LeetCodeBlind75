from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        map = defaultdict(list)
        R = len(nums)
        C = len(nums[0])

        for r in range(R):
            Col = len(nums[r])
            for c in range(Col):
                key = r + c
                # print(key, nums[r][c])
                map[key].append(nums[r][c])
        print(map)

        ans = []
        for k,v in map.items():
            ans.extend(v[::-1])
        return ans 

       