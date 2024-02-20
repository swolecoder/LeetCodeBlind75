class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, 0
        ans = 0

        while j < len(nums):
            if nums[i] < nums[j] and i != j:
                i +=1
                ans +=1
            j +=1
        return ans
        