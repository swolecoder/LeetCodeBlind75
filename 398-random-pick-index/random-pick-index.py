from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for index, num in enumerate(nums):
            self.map[num].append(index)

        

    def pick(self, target: int) -> int:
        if target not in self.map:
            return -1
        value = self.map[target]
        # print(value)
        index = random.randint(0,len(value)-1)
        # print(index)
        return value[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)