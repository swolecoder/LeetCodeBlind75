class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        s1 = set(nums1)
        s2 = set(nums2)


        ans = []
        count = 0

        for num in nums1:
            if num in s2:
                count +=1
        ans.append(count)
        count = 0

        for num in nums2:
            if num in s1:
                count +=1
        ans.append(count)

        return ans 

        