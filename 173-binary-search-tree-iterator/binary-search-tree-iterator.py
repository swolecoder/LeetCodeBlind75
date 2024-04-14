# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.data = deque()
        self.dfs(root)
    


    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.left)
        self.data.append(root.val)
        self.dfs(root.right)
        

    def next(self) -> int:
        if self.data:
            return self.data.popleft()

        return -1

        

    def hasNext(self) -> bool:
        if self.data:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()