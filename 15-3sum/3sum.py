class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        total = 0

        for i in range(len(nums)):
            l = i +1
            r = len(nums) -1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum > 0 :
                    r -=1
                elif sum < 0:
                    l +=1
                else:
                    ans.append([nums[i] ,nums[l] ,nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while r > l and nums[r] == nums[r-1]:
                        r -=1
                    l +=1
                    r -=1
        return ans 
        