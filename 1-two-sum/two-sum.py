class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            y = target -nums[i] 

            if y in map:
                return [map[y], i]
            map[nums[i]] = i
        return [-1,-1]
        