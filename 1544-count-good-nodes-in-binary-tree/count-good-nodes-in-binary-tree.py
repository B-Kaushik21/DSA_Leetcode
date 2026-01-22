# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        curr=float('-inf')
        self.res=0
        def dfs(root,curr):
            if curr<=root.val:
                curr=root.val
                self.res+=1
            if root.left:
                dfs(root.left,curr)
            if root.right:
                dfs(root.right,curr)
        dfs(root,curr)
        return self.res