# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def maxpathdown(root,maxi):
            if not root:
                return 0
            left=max(0,maxpathdown(root.left,maxi))#avoid neg value if found return 0
            right=max(0,maxpathdown(root.right,maxi))
            self.maxi=max(self.maxi, left+right+root.val)
            return root.val+max(left,right) #adding node val which is maximum of left,right
        maxpathdown(root,self.maxi)
        return self.maxi