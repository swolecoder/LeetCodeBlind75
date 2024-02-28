class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minFound = float("inf")
        current = 0
        i = 0

        for j in range(len(nums)):
            current += nums[j]

            while current >= target:
                minFound = min(minFound,j -i +1)
                current -= nums[i]
                i +=1

        return 0 if minFound == float("inf") else minFound
    



        