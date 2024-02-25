class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()

        # ans = []

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         ans.append(i)
        # return ans 
        lessThanEqual = 0
        less = 0

        for  n in nums:
            if n <= target:
                lessThanEqual +=1
            if n < target:
                less +=1
        
        return list(range(less,lessThanEqual))
        