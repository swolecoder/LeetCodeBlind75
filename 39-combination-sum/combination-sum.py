class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []


        def helper(nums, target, current):
            nonlocal ans

            if target < 0 or not nums:
                return 
            if target == 0:
                ans.append(current)
                return 

            include_first = helper(nums, target - nums[0], current + [nums[0]])

            not_inclusde = helper(nums[1:],target ,  current)
            
        #     for i in range(len(nums)):
        #         left = target - nums[i]
        #         if left >= 0:
        #             helper(nums,left, current + [nums[i]])
        
        helper(candidates, target, [])
        # print(ans)

        return ans


        