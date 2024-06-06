from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)

        data = [ [] for _ in range(len(nums) + 1)]
        print(map)

        for key, val in map.items():
            data[val].append(key)
        print(data)

        ans = []

        for i in range(len(data)-1,-1,-1):
            if len(data[i]) > 0:
                for j in range(len(data[i])):
                    ans.append(data[i][j])
                    if len(ans) == k:
                        return ans
            
        