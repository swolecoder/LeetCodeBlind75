class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(nums, perm,track):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for i in range(len(nums)):
                if track[i]:
                    continue
                perm.append(nums[i])
                track[i] = True
                dfs(nums,perm,track)

                track[i] = False
                perm.pop()
        
        dfs(nums,[], [False]* len(nums))
        return res 
