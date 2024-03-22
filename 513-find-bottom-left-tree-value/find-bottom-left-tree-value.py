# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.val=root.val
        self.maxl=0
        def dfs(root,currl):
            if(root==None):
                return
            if(currl>self.maxl):
                self.maxl=currl
                self.val=root.val
            dfs(root.left,currl+1)
            dfs(root.right,currl+1)
        dfs(root,0)
        return self.val
            