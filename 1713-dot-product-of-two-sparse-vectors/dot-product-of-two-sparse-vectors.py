class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.map[i] = nums[i]
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        map1 = self.map

        map2 = vec.map
        ans = 0

        for k, v in map1.items():
            if k in map2:
                val = v * map2[k]
                ans += val
        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)