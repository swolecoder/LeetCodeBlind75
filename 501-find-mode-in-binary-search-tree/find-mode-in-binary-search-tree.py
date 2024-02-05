# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]: 
        ans = []

        c = 0
        seen= None
        m = 0

        def helper(root):
            nonlocal ans, c, m , seen

            if not root:
                return 
            
            helper(root.left)

            if seen == root.val:
                c +=1
            else:
                c = 1
                seen = root.val
            
            if c > m:
                m = c
                ans = [root.val]
            elif c == m:
                ans.append(root.val)

                


       
            print(ans)
            helper(root.right)
        
        helper(root)
        return ans
        