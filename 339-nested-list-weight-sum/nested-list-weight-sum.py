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
from collections import deque
class Solution:
    def __init__(self):
        self.ans = 0

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # self.depth(nestedList)
        # return self.ans

        ans = 0
        q = nestedList
        level = 1
        while q:

            nextItem = []
            length = len(q)
            for i in range(length):
                node = q.pop(0)
                if node.isInteger():
                    ans += node.getInteger() * level 
                else:
                    nextItem.extend(node.getList())
            
            level +=1
            q = nextItem
        return ans








    # def depth(self, nums, level=1):

    #     for n in nums:
    #         if n.isInteger():
    #             self.ans += n.getInteger() * level
    #         else:
    #             self.depth(n.getList(), level + 1)

        