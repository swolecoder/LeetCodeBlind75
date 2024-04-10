class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if not nums:
            return -1

        if len(nums) == 1:
            return 0
        
        l = 0
        r = len(nums)-1

        while l <= r:

            mid = (l +r)//2

            if mid +1 < len(nums) and l >= 1 and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid 

            if mid +1 < len(nums) and nums[mid] < nums[mid+1]:
                l = mid +1
            else:
                r = mid -1
        
        return l
        
        #  [1,2,3,1]
        #   l.     r

        #   0 + 3 // 2-> 2

