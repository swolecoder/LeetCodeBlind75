class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        longest_sequence = 0

        for i in range(len(nums)):
            current = nums[i] -1
            if current not in seen:
                curr = nums[i]
                count = 1 
                while curr + count  in seen:
                    count +=1
                
                longest_sequence = max(longest_sequence, count)
        return longest_sequence
        