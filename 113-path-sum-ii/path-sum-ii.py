# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def helper(root,curr,path):
            if not root:
                return
            path.append(root.val)
            curr-=root.val
            #leaf node
            if not root.left and not root.right:
                if curr==0:
                    res.append(path[:])
            else:
                helper(root.left,curr,path)
                helper(root.right,curr,path)
            path.pop()#baktracking
        helper(root,targetSum,[])
        return res