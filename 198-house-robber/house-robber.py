class Solution:
    def rob(self, nums: List[int]) -> int:


        def helper(nums, index , memo):
            if index in memo:
                return memo[index]
            if not nums or index >= len(nums):
                return 0

            

            first_house = nums[index] + helper(nums, index+2, memo) #if index + 2 < len(nums) else 0
            skip_first_house =  helper(nums, index+1, memo) #if index + 1 < len(nums) else 0

            memo[index] = max(first_house, skip_first_house)
            return memo[index]
        
        return helper(nums, 0,{})
        