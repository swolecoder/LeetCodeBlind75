class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)

        num = 1
        for i in range(len(left)):
            left[i] = num 
            num *= nums[i]
        
        print(left)
        num = 1
        for i in range(len(nums)-1,-1,-1):
            left[i] = left[i] *num
            num *= nums[i]
        return left 