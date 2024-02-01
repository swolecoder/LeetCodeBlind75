class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = {}

        for i in range(len(self.nums)):
            if self.nums[i]:
                self.map[i] = self.nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0

        for i in vec.map:
            if i in self.map:
                ans += self.map[i] * vec.map[i]
        return ans


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)