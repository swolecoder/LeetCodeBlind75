# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        curr = root
        while curr:
            self.list.append(curr)
            curr = curr.left
        

    def next(self) -> int:
        curr = self.list.pop()
        node = curr.right
        while node:
            self.list.append(node)
            node = node.left


        return curr.val
        

    def hasNext(self) -> bool:
        return len(self.list) != 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()