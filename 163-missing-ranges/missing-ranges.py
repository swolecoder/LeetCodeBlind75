class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        num = [lower-1] + nums + [upper +1]
        ans = []

        for i in range(1,len(num)):
            diff = num[i]- num[i-1]
            if diff > 1:
                ans.append([num[i-1]+1, num[i]-1])
        return ans
