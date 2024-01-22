class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf') , float('inf')

        for l in range(len(nums)):
            if nums[l] <= i:
                i = nums[l]
            elif nums[l] <= j:
                j = nums[l]
            else:
                return True
        return False
        