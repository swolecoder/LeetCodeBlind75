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
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        q = deque([(item, 1) for item in nestedList])  # Initialize queue with the list and level 1
        ans = 0

        while q:
            nextItem, level = q.popleft()  # Get the next item and its level
            if nextItem.isInteger():
                ans += nextItem.getInteger() * level  # If it's an integer, add to the sum
            else:
                # If it's a list, extend the queue with the items in the list, each with incremented level
                for item in nextItem.getList():
                    q.append((item, level + 1))
        
        return ans



        