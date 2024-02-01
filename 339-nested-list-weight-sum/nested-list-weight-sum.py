# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # depth = 1

        # q =nestedList
        # ans = 0

        # while q:
        #     length = len(q)
        #     nextItem= []
        #     for i in range(length):
        #         data = q.pop(0)
        #         if data.isInteger():
        #             ans += data.getInteger() * depth
        #         else:
        #             nextItem.extend(data.getList())
        #     q = nextItem
        #     depth +=1
        # return ans
        ans = 0

        def dfs(items, depth=1):
            nonlocal ans

            for item in items:
                if item.isInteger():
                    ans += item.getInteger() * depth
                else:
                    dfs(item.getList(), depth +1)
        dfs(nestedList)
        return ans


        