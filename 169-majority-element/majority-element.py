class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # [3,2,3]
        
        res = nums[0]
        count = 1

        for i in range(1,len(nums)):

            if count == 0:
                res = nums[i]
                count = 1
            
            else:

                if res == nums[i]:
                    count +=1
                else:
                    count -=1
        
        return res