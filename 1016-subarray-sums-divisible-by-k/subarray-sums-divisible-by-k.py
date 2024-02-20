class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        map = {0 : 1}
        running_sum = 0
        ans = 0

        for n in nums:
            running_sum += n
            remain = running_sum % k
            ans += map.get(remain,0)
            map[remain] = map.get(remain,0) +1
        
        return ans

        