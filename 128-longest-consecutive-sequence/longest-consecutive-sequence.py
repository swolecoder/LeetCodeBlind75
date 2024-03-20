class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        seen = set(nums)

        for num in nums:
            #starting point
            if num -1 not in seen:
                start = 0
                while num +start in seen:
                    start +=1
                
                ans = max(ans , start)
        return ans

        