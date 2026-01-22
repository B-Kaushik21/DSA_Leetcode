# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        def search(root,path,res):
            if (root.left==None) and (root.right==None):
                res.append(path+str(root.val))
            if root.left!=None:
                search(root.left,path+str(root.val)+"->",res)
            if root.right!=None:
                search(root.right,path+str(root.val)+"->",res)
        if root:
            search(root,"",res)
        return res          
        