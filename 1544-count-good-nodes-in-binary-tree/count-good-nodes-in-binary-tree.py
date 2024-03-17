# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count=0

        def dfs(root,currmax):
            if(root==None):
                return
            if(root.val>=currmax):
                self.count+=1
            dfs(root.left,max(currmax,root.val))
            dfs(root.right,max(currmax,root.val))
        dfs(root,float("-inf"))
        return self.count