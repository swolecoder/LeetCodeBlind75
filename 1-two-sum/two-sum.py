from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for i in range(len(nums)):
            y = target  - nums[i]
            if y in hashMap:
                return [hashMap[y], i]
            hashMap[nums[i]] = i
        
        return [-1,-1]