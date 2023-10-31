class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [0] * len(nums)
        num = 1

        for i in range(len(nums)):
            left[i] = num
            num *= nums[i]
        
        num = 1
        for i in range(len(nums)-1,-1,-1):
            left[i] = num * left[i]
            num *= nums[i]
        
        return left
