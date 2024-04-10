from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)

        sum = 0
        ans = 0
        prefix[0] = 1


        for n in nums:
            sum += n

            looking = sum - k

            if looking in prefix:
                ans += prefix.get(looking,0)
            
            prefix[sum] = prefix[sum] +1
        
        print(prefix)
        return ans


        