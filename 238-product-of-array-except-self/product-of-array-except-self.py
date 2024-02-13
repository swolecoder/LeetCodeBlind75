class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [0] * len(nums)

        curr = 1

        for i in range(len(nums)):
            left[i] = curr
            curr *= nums[i]
        
        curr = 1
        for j in range(len(nums)-1,-1,-1):
            left[j] = left[j] * curr
            curr = curr * nums[j]

        return left        