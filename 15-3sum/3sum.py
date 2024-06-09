class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if not nums:
            return res

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:

                ans = nums[i] + nums[j] + nums[k]
                if ans == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    while j < len(nums)-1 and j < k and nums[j] == nums[j+1]:
                        j +=1
                    
                    while k > 0 and k > j and nums[k] == nums[k-1]:
                        k -=1
                    
                    j +=1
                    k -=1
                elif ans > 0:
                    k -=1
                else:
                    j +=1
            

        return res
        