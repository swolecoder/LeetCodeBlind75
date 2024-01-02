class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:


        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

        # return nums + nums
#         ans = []

# #  Time Complexity => O(n):
# # The operation nums + nums takes O(n) time, where n is the length of the list nums. This is because adding two lists in Python involves creating a new list and copying over the elements from the two original lists.
# # Space Complexity => O(n):
# # The function returns a new list that has twice the size of the original list nums. Hence, the space complexity is O(n).

#         for i in range(2):
#             for n in nums:
#                 ans.append(n)
#         return ans



        