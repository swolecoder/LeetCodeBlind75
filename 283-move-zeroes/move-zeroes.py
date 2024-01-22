class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[r], nums[i] = nums[i], nums[r]
                r +=1
        
        