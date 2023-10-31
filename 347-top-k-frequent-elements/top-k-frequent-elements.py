class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = Counter(nums)

        data = [ [] for i in range(len(nums) +1)]

        for key, val in map.items():
            data[val].append(key)
        
        ans = []

        for i in range(len(data)-1,-1,-1):
            for n in data[i]:
                    ans.append(n)
                    if len(ans) == k:
                        return ans
        
        
        
        print(data)