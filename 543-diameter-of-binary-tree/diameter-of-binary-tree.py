# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def height(root):
            if not root:
                return 0
            l_height=height(root.left)
            r_height=height(root.right)
            self.diameter=max(self.diameter,l_height+r_height)
            return 1+max(l_height,r_height)
        height(root)
        return self.diameter