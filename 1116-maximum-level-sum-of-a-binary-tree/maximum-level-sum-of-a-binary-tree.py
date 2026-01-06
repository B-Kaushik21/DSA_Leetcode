# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxi=-float('inf')
        level=0
        maxLevel=0
        q=deque()
        q.append(root)
        while q:
            level+=1
            sum=0
            for _ in range(len(q)):
                node=q.popleft()
                sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if maxi<sum:
                maxi,maxLevel=sum,level
        return maxLevel