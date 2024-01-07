class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        window = k-1
        res = float("inf")
        r =0

        while window < len(nums):
            res = min(res, nums[window]- nums[r])
            window +=1
            r +=1
        

        return res



        