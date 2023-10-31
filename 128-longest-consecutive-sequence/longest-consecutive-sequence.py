class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set()
        for n in nums:
            seen.add(n)

        res = 0

        for i in range(len(nums)):

            if nums[i] -1 not in seen:
                count = 1

                while nums[i]+count in seen:
                    count +=1
                res = max(count, res)
        
        return res
        