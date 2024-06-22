class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left + right)//2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right -=1
            else:
                left += 1
        return -1
        
        