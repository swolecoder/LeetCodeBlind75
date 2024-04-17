# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:


        def dfs(node, path):
            if not node:
                return
            
            # Convert node's value to corresponding alphabetic character
            char = chr(node.val + ord('a'))
            # Add current character to the path
            path += char
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                # Reverse path to form the correct string from leaf to root
                current_path = path[::-1]
                # Update smallest string if the new one is lexicographically smaller
                nonlocal smallest
                if current_path < smallest:
                    smallest = current_path
            
            # Continue DFS to the left and right children
            dfs(node.left, path)
            dfs(node.right, path)
        
        # Initialize smallest to a very high value in the lexicographical order
        smallest = '{'  # Using '{' because it is higher than any lowercase letter
        # Start DFS from the root with an empty path string
        dfs(root, "")
        return smallest
        