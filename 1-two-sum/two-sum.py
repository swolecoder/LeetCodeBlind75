from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)

        for index , num in enumerate(nums):
            y = target - num
            print(num, index)
            if y in map:
                return [map[y], index]
            map[num] = index
        
        return []
        